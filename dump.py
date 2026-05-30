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

# edid-decode < /home/ubuntu/edid_verify.bin
