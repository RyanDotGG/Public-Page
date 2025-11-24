# A int is 32 bits, or 4 bytes
# A long is 64 bits, or 8 bytes
# A timestamp is a 32-bit Unix Timestamp, or 4 bytes

# big end >
# 4 bytes I
# 8 bytes Q
# 1 byte  B

# >[header-->]lcii[hostname]i[flag]i[body-->]iiii
from pathlib import Path
import struct
import datetime
import base64
import ipaddress

filepath = "C:/Users/[FILEPATH]"
text_ = Path(filepath)
binarydata = text_.read_bytes()
#hexdata = ''.join(map('{:02X}'.format, binarydata))
offset = 0
magic_bytes, version, start_time, hostname_length = struct.unpack_from(">QBII",binarydata, offset)
offset = 17

magic_bytes = hex(magic_bytes)
start_time = datetime.datetime.fromtimestamp(start_time)

hostname = (struct.unpack_from(f">{hostname_length}s", binarydata, offset)[0]).decode("utf-8")
offset += hostname_length

flag_length = struct.unpack_from(">I", binarydata, offset)[0]
offset += 4

flag = base64.b64decode(struct.unpack_from(f">{flag_length}s", binarydata, offset)[0]).decode("utf-8")
offset += flag_length

number_of_entries = struct.unpack_from(">I", binarydata, offset)[0]
offset += 4

entries = []
for entry in range(number_of_entries):
    current_entry = struct.unpack_from(">IIII", binarydata, offset)
    as_dictionary = {"source_ip":ipaddress.ip_address(current_entry[0]),
                     "destination_ip":ipaddress.ip_address(current_entry[1]),
                     "timestamp":datetime.datetime.fromtimestamp(current_entry[2]),
                     "bytes_transferred":current_entry[3]}
    entries.append(as_dictionary)
    offset += 16

print("writting to file")
filepath = "C:/Users/[FILEPATH]/outfile.txt"
text_ = Path(filepath)
with text_.open("a") as text_:
    text_.write(f"Magic Bytes: {magic_bytes}"+"\n")
    text_.write(f"Version: {version}"+"\n")
    text_.write(f"Start Time: {start_time}"+"\n")
    text_.write(f"Hostname Length: {hostname_length}"+"\n")
    text_.write(f"Hostname: {hostname}"+"\n")
    text_.write(f"Flag Length: {flag_length}"+"\n")
    text_.write(f"Flag: {flag}"+"\n")
    text_.write(f"Number of Entries: {number_of_entries}"+"\n")
    for entry in entries:
        output =""
        for value in entry.values():
            output += str(value) + "\t"
        text_.write(output+"\n")
print("done")
