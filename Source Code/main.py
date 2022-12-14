
#  Copyright Rubya Afrin, 2022 Licensed under MIT License.
#  See the LICENSE.txt for more information.import sys
sys.path.append('../')
import log_parsing

input_dir    = '../Dataset/HDFS/' # The input directory
output_dir = 'logparse_result/' # The result directory
log_filepath = input_dir + 'HDFS_2k.log' # The input log file path
log_format = '<Date> <Time> <Pid> <Level> <Component>: <Content>' # HDFS log format
n_workers = 1 # The number of workers in parallel
template_filepath = log_filepath + '_templates.csv' # The event template file path


if __name__ == "__main__":
    matcher = log_parsing.PatternMatch(outdir=output_dir, n_workers=n_workers, logformat=log_format)
    matcher.match(log_filepath, template_filepath)
