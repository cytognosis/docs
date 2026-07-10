* Read this deep research doc (/home/mohammadi/Downloads/Multi-Trait GWAS Analysis Methods.md), generated in response to the prompt "Find best and/or most recent/well-cited methods to factorize/embed GWAS summary stats across multiple related indications, computing polygenic risk scores for factors, reconciling GWAS sumstats (including per individual symptoms/phenotypes of a disease, particularly related to mental health and neuro-indications), and/or methods that do the same using individual level genotypes (WGS or SNP arrays), or, methods jointly analysing GWAS sumstats and individual genotypes)"

* Then read /home/mohammadi/Claude/Projects/Grants/04-research/AI_ML_dimensional_biotyping_landscape_2026.md and focus on the parts relevant to genomics
* Then read our our previous research on multimodal models using genomics and connectomics (and also relevant parts from above doc on multimodal)
* Summarize all above and expand on it, focusing on most well-cited tools, models, latest development, both using traditional genomics/statgen methods, and novel deep learning approaches most relevant for us, and then use it as seed to expand upon it
* Expand it to also include /special interest in: 
  * the use of Genomic foundation models (including but not limited to AlphaGenome and Evo 2) and fine-tuning them for these applications (in particular for neuro-indications)
  * use of sparse LD/precision matrix such as LDGM (including methods in [graphld](https://github.com/oclb/graphld) and [score](https://github.com/freeseek/score)) to allow more efficient accounting for SNP covariance structure
  * Use of Pangenome
  * Use of multi-trait summary stats including:
    * Generic, more comprehensive panels (such as [Pan-UKBB](http://pan.ukbb.broadinstitute.org/)), and neuro-focused ones, including our recent work on tailored cross-neuro gwas summary stats from PGC and similar (e.g., NeuroGWAS)
  * Models incorporating network and pathway priors to enhance interpretability of genomic factors
  * Methods focusing on disentangling / factorizing genomic variants into biologically meaningful, pathway enriched axes