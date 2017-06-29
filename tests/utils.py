import subprocess

def run_shell_cmd(cmd):
    """ Run a shell command , capture and return the return code
    of the shell call

    cmd : str ; the command to run
    """

    proc = subprocess.Popen(cmd,shell=True)
    proc.wait()
    return proc.returncode


def compare_with_tolerance(base,num,tolerance):
    """ Compare two numbers and allow some tolerance in the deviation

    base : float ; the known truth value
    num : float ; the value obtained from the test run
    tolerance : float ; the permissible deviation from base
    """

    return abs(base - num)/(base) <= tolerance


def parse_summary_file(summary_file):
    """ Parse a summary file generated by this pipeline
    and return the metrics as a dictionary {"metric":val}
    summary_file : str; the path to the summary file
    """

    metrics = {}
    with open(summary_file,"r") as IN:
        for line in IN:
            contents = line.strip('\n').split('\t')
            if len(contents)!=2:
                raise Exception("Could not parse %s, encountered greater than two columns!\n"%summary_file)
            else:
                val,key = contents
                if key in metrics:
                    raise Exception("Could not parse %s, Encountered duplicate metric in the same file !\n"%summary_file)
                else:
                    metrics[key] = float(val)

    return metrics
