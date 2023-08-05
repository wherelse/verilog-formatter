import os
import argparse

# if you want to modify the format parameter, you can change it below.
# the details of parameter reference: https://chipsalliance.github.io/verible/verilog_format.html
format_parameter = '--column_limit=200 --indentation_spaces=2'

parser = argparse.ArgumentParser(description='format verilog by verible')
parser.add_argument('--input', '-i', help='input filelist(.f) file', required=True)
args = parser.parse_args()

with open(args.input, mode="r") as filelist:
    filepaths = filelist.readlines()
    for filepath in filepaths:
        if(filepath):
            # print("./verible-verilog-format --inplace {0} {1}".format(format_parameter,filepath))
            os.popen("./verible-verilog-format --inplace {0} {1}".format(format_parameter,filepath))
                               
filelist.close()
print("format verilog done")