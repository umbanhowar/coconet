#!/bin/bash

source /gpfs/data/drlab/nate/magenta-env/bin/activate

set -x
set -e

# Pass path to checkpoint directory as first argument to this script.
# You can also download a model pretrained on the J.S. Bach chorales dataset from here:
# http://download.magenta.tensorflow.org/models/coconet/checkpoint.zip
# and pass the path up to the inner most directory as first argument when running this
# script.
#checkpoint=$1
checkpoint="/data/drlab/nate/magenta/magenta/models/coconet/logs/straight-32-64_bs=5,corrupt=0.5,len=200,lr=0.0625,mm=orderless,num_i=4,n_pch=128,mask_only=False,quant=0.125,rescale=True,sep=True,res=True,soft=False"

# Change this to path for saving samples.
generation_output_dir="/gpfs/data/drlab/nate/magenta/magenta/models/coconet/samples"

# Generation parameters.
# Number of samples to generate in a batch.
gen_batch_size=1
piece_length=64
strategy=igibbs

# Run command.
bazel run :coconet_sample \
-- \
--checkpoint="$checkpoint" \
--gen_batch_size=$gen_batch_size \
--piece_length=$piece_length \
--temperature=0.5 \
--strategy=$strategy \
--generation_output_dir=$generation_output_dir \
--logtostderr

#--temperature=0.99 \
