# pararun 
pararun is a python package to generate and run bash scripts for parallel or iterative jobs.


## Table of Contents

- [Overview](#overview)
- [Requirements](#requirements)
- [Examples](#examples)

####

## <a name="overview"></a>Overview
Pararun package contains two scripts:
- **runpara.py**: run **para**llel jobs for input files with same suffix, like for "liba.fastq" and "libb.fastq"
- **runiter.py**: run **iter**ative jobs by renaming the first round input to something like "ref_round0.fasta"


## <a name="requirements"></a>Requirements

- python 3 (or python >=2.7)

## Installation
```bash
# for python3, you can use pip to install
pip install pararun
# if you prefer not to use pip, or you are using python2, you can directly use the script
git clone https://github.com/Runsheng/pararun.git
export PATH="./pararun/pararun/":$PATH
# after the installtion, you can run runiter.py and runpara.py from your shell
runpara.py --help
usage: runpara [-h] [-f FOLDER] [-s SUFFIX] [-p CORE] [-c CMD] [-n DRYRUN]
Run bash cmd lines for files with the same surfix
optional arguments:
  -f FOLDER, --folder FOLDER
                        the folder containing all files
  -s SUFFIX, --suffix SUFFIX
                        the suffix of the files
  -p CORE, --core CORE  the cores used
  -c CMD, --cmd CMD     the cmd to run, with prefix as prefix
  -n DRYRUN, --dryrun DRYRUN
                        use dry run to output

runiter.py --help
usage: runiter [-h] [-r ROUND] [-c CMD] [-0 KEY0] [-1 KEY1] [--resume RESUME]
optional arguments:
  -r ROUND, --round ROUND
                        how many round will this cmd runs
  -c CMD, --cmd CMD     the cmd line to be run, with round0 and round1 indicating the iter items
  -0 KEY0, --key0 KEY0  the indicator of the key for iter0, need to have a 0 inside
  -1 KEY1, --key1 KEY1  the indicator of the key for iter1, need to have a 1 inside
  --resume RESUME       try to resume the former run by find the max round
```


## <a name="examples"></a>Examples
### Examples for runpara
```bash

# for a folder containing multiple bed files and one nr3c1exon.gtf file
# you want to run bedtools intersect to get intersections for all your bed files in your current dir with the nr3c1exon.gtf region
runpara.py -f . -s bed -p 20 -c "bedtools intersect -a prefix.bed -b nr3c1exon.gtf -wa | uniq > prefix_nr3c1.bed"
# example to run bwa mem mapping for all fastq files in one dir 
runpara.py -f . -s fastq -p 1 -c "bwa mem -t 32 ref.fasta prefix.fastq | samtools view -bS > prefix.bam"

```


## Citation