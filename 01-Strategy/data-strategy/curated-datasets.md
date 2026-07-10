

* https://brain-map.org/bkp
* Allen

# Cellular

> **Status**: Active
> **Date**: 2026-07-10
> **Author**: @shahin
> **Audience**: leadership
> **Tags**: `strategy`
> **Variants**: Technical (this doc) - Readable (Obsidian twin optional, same filename) - Agent (n/a)

## In vivo

### Human Neural Organoid Cell Atlas (HNOCA)

* Paper: [An integrated transcriptomic cell atlas of human neural organoids](https://www.nature.com/articles/s41586-024-08172-8)

* Website: https://devsystemslab.github.io/HNOCA-tools/

* Zenodo link: https://zenodo.org/records/14161275

* Census collection link: https://cellxgene.cziscience.com/collections/de379e5f-52d0-498c-9801-0f850823c847

  * Notes: The metadata field `cell_type` corresponds to a manual mapping of the original author annotations (metadata field `cell_type_original`) to the Cell Ontology. For the harmonised cell type, region, and neurotransmitter-transporter annotations, please refer to the metadata fields starting with `annot_` in the Author Categories. 2. For the HNOCA extended, you can find the harmonised cell type annotation covering all cells (including the extension datasets) in the `annot_level_2_extended` metadata field. 3. The metadata field `tissue` corresponds to the target tissue of the employed organoid differentiation protocol. For example, a cell originating from a sample generated using a cortical differentiation protocol will be annotated as `cerebral cortex`. 4. The data deposited here contains slightly fewer cells than in the data associated with the original publication. This is due to the removal of some cells with identical expression values as required by the CellxGene schema. You can find the full object at the Zenodo Data Source link to the right. PUBLICATION ABSTRACT: Neural tissues generated from human pluripotent stem cells in vitro (known as neural organoids) are becoming useful tools to study human brain development, evolution and disease. The characterization of neural organoids using single-cell genomic methods has revealed a large diversity of neural cell types with molecular signatures similar to those observed in primary human brain tissue. However, it is unclear which domains of the human nervous system are covered by existing protocols. It is also difficult to quantitatively assess variation between protocols and the specific cell states in organoids as compared to primary counterparts. Single-cell transcriptome data from primary tissue and neural organoids derived with guided or un-guided approaches and under diverse conditions combined with large-scale integrative analyses make it now possible to address these challenges. Recent advances in computational methodology enable the generation of integrated atlases across many data sets. Here, we integrated 36 single-cell transcriptomics data sets spanning 26 protocols into one integrated human neural organoid cell atlas (HNOCA) totaling over 1.7 million cells. We harmonize cell type annotations by incorporating reference data sets from the developing human brain. By mapping to the developing human brain reference, we reveal which primary cell states have been generated in vitro, and which are under-represented. We further compare transcriptomic profiles of neuronal populations in organoids to their counterparts in the developing human brain. To support rapid organoid phenotyping and quantitative assessment of new protocols, we provide a programmatic interface to browse the atlas and query new data sets, and showcase the power of the atlas to annotate new query data sets and evaluate new organoid protocols. Taken together, the HNOCA will be useful to assess the fidelity of organoids, characterize perturbed and diseased states and facilitate protocol development in the future.

    ![image-20260514171414290](image-20260514171414290.png)

### Additional

* [Single-cell transcriptomics revealed molecular vulnerability in a human midbrain-like organoid model of Parkinson’s disease](https://www.cell.com/iscience/fulltext/S2589-0042(26)00049-0)



## Perturbational

* PerturbAI dataset
  * Description: An in vivo gene expression functional atlas across the **mouse brain**. Includes the transcriptome-wide responses to loss of **1,947 disease-associated genes**, profiling over **7.7 million cells** spanning **major brain regions** and neuronal populations
  * Data: https://huggingface.co/datasets/perturbai/wholebrain_crispr_atlas
  * Website: https://www.perturb.ai/
  * Paper: [Genome-scale functional mapping of the mammalian whole brain with in vivo Perturb-seq](https://www.biorxiv.org/content/10.64898/2026.03.16.711480v1)

![PerturbAI](figures/PerturbAI.png)
