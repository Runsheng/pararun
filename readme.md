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
runiter.py --help
runpara.py --help
```


## <a name="examples"></a>Examples
```bash
# test if all dependencies are installed
trackrun.py test --install

# generate the read track from minimap2 bam file
bam2bigg.py -b group1.bam -o group1.bed
bam2bigg.py -b group2.bam -o group2.bed

# merge the bed file and sort
cat group1.bed group2.bed > read.bed
bedtools sort -i read.bed > reads.bed

# Examples for running commands:
trackrun.py clusterj -s reads.bed -r refs.bed -t 40 # run in junction mode, generate the isoform.bed
trackrun.py count -s reads.bed -r refs.bed -i isoform.bed # generate the csv file for isoform expression
trackrun.py desc --isoform isoform.bed --reference ref.bed > desc.bed  # generate the description for each novel isoform

# alternative for cluster
trackrun.py cluster -s reads.bed -r refs.bed -t 40 # run in exon/intron intersection mode， slower
```


## Citation
Please kindly cite our paper in Genome Research if you use trackcluster in your work.

Li, R., Ren, X., Ding, Q., Bi, Y., Xie, D. and Zhao, Z., 2020. Direct full-length RNA sequencing reveals unexpected transcriptome complexity during *Caenorhabditis elegans* development. **Genome research**, 30(2), pp.287-298.