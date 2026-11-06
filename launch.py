#!/usr/bin/env python3
"""Launch the demo using your installed WHDLoad boot files and Kickstart ROMs."""
from pathlib import Path
import argparse,hashlib,os,re,shutil,subprocess,zipfile
ROOT=Path(__file__).resolve().parent
HOME=Path.home()
def whdboot(given):
 candidates=[given]if given else []
 candidates += [HOME/'.local/share/uae4arm2026/WHDBoot',HOME/'.local/share/amiberry/whdboot',HOME/'Amiberry/whdboot',Path('/usr/share/amiberry/whdboot')]
 for p in candidates:
  if p and (p/'WHDLoad').is_file() and (p/'boot-data.zip').is_file():return p
 raise SystemExit('Install Amiberry WHDBoot, or pass --whdboot DIRECTORY containing WHDLoad and boot-data.zip.')
def prepare(a):
 installed=whdboot(a.whdboot);kicks=installed/'save-data/Kickstarts'
 candidates=[a.kickstart]if a.kickstart else []
 candidates += [HOME/'Amiberry/ROMs/kick31.rom',kicks/'kick40068.A1200']
 kick=next((p for p in candidates if p and p.is_file() and hashlib.sha1(p.read_bytes()).hexdigest()=='e21545723fe8374e91342617604f1b3d703094f1'),None)
 if kick is None:raise SystemExit('Pass --kickstart PATH to your original A1200 Kickstart40.068 ROM.')
 rtb=kicks/'kick40068.A1200.RTB'
 if not rtb.is_file():raise SystemExit('Your WHDBoot save-data/Kickstarts needs kick40068.A1200.RTB.')
 host=a.host_rom or (kick if a.cpu=='020' else kicks/'kick40068.A4000')
 if not host.is_file():raise SystemExit('Pass --host-rom PATH to your A4000 Kickstart ROM for the040 profile.')
 boot=ROOT/'.local/boot';boot.mkdir(parents=True,exist_ok=True)
 with zipfile.ZipFile(installed/'boot-data.zip')as archive:archive.extractall(boot)
 for folder in ['C','S','Devs/Kickstarts']:(boot/folder).mkdir(parents=True,exist_ok=True)
 for old in (boot/'S').iterdir():
  if old.name.casefold()=='startup-sequence':old.unlink()
 shutil.copy2(installed/'WHDLoad',boot/'C/WHDLoad')
 shutil.copytree(ROOT/'BubbleBobbleDemo',boot/'BubbleBobbleDemo',dirs_exist_ok=True)
 shutil.copy2(kick,boot/'Devs/Kickstarts/kick40068.A1200');shutil.copy2(rtb,boot/'Devs/Kickstarts'/rtb.name)
 (boot/'S/Startup-Sequence').write_text('FailAt25\nCD DH0:BubbleBobbleDemo\nC:WHDLoad SLAVE=BubbleBobble.slave NOMMU CACHE SplashDelay=100\n'.replace('FailAt25','FailAt 25'))
 name='A1200-020.uae'if a.cpu=='020'else'A4000-040.uae'
 text=(ROOT/'configurations'/name).read_text()
 text=re.sub(r'(?m)^kickstart_rom_file=.*$',lambda _:'kickstart_rom_file='+str(host.resolve()),text)
 text+=f'\nfilesystem2=rw,DH0:BOOT:{boot},0\nuaehf0=dir,rw,DH0:BOOT:{boot},0\n'
 config=ROOT/'.local'/name;config.write_text(text);return config
if __name__=='__main__':
 p=argparse.ArgumentParser(description=__doc__)
 p.add_argument('--cpu',choices=['020','040'],default='020');p.add_argument('--kickstart',type=Path);p.add_argument('--host-rom',type=Path);p.add_argument('--whdboot',type=Path);p.add_argument('--prepare-only',action='store_true');p.add_argument('--emulator',default=os.environ.get('AMIBERRY_BIN','amiberry'))
 a,extra=p.parse_known_args();config=prepare(a);print(config)
 if not a.prepare_only:raise SystemExit(subprocess.call([a.emulator,'-G','-f',str(config),*extra]))
