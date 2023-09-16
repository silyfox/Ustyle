#!/bin/bash

for id in `cat id.txt`; do
	cp demo_final_2/cset_ptx/db2_wavs/$id* cset/
	cp demo_final_2/fg_v8_1116/db2_wavs/$id* m3/
	cp demo_final_2/gradtts_datspk_deccatedspkemo/db2_wavs/$id* grad-c/
	cp demo_final_2/proposed_neu/db2_wavs/$id* proposed/
done
