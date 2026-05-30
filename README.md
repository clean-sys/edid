REQ: sudo apt install -y i2c-tools edid-decode read-edid chromium wxedid

Dump: 
```
python3 -c "
import subprocess, time
data = []
for i in range(256):
    r = subprocess.run(['sudo','i2cget','-y','4','0x50',hex(i),'b'],
        capture_output=True, text=True)
    data.append(int(r.stdout.strip(),16))
    time.sleep(0.005)
open('/home/ubuntu/edid_verify.bin','wb').write(bytes(data))
"

//edid-decode < /home/ubuntu/edid_verify.bin
```

Write:
```
python3 -c "                       
import subprocess, time, sys

EDID_FILE = '/home/ubuntu/edid_COMPILED.bin'
BUS = '4'
ADDR = '0x50'

data = open(EDID_FILE,'rb').read()
print(f'Writing {len(data)} bytes...')
for i, byte in enumerate(data):
    r = subprocess.run(['sudo','i2cset','-y',BUS,ADDR,hex(i),hex(byte),'b'],
        capture_output=True)
    if r.returncode != 0:
        print(f'Error at byte {i}')
        sys.exit(1)
    time.sleep(0.01)
    if i % 32 == 0: print(f'  {i}/256...')
print('Done!')
"
```
