## 99. Consolidated references and verification status

All references are drawn directly from source documents (SCIENCE_BRIEF.md, IGoR_TA1_TA2_Research_2026-06-02.md, IGoR_TA1-TA2_Methods_DeepDive_2026-06-05.md, PRIOR_WORK_CONSOLIDATED.md, full_proposal/FULLPROPOSAL_DRAFT.md). Items marked (verify) require an independent check against arXiv, PubMed, or journal DOI lookup before submission. Items marked (internal) are not for distribution.

---

### Virtual cell and world models

1. Bunne C, Roohani Y, Rosen Y, et al. How to build the virtual cell with artificial intelligence: priorities and opportunities. *Cell*. 2024;187(25):7045-7063. doi:10.1016/j.cell.2024.11.015. [NOTE: a separate draft cited Cell 189(7):1175-1188; verify volume and pages, see inconsistency flag in PRIOR_WORK_CONSOLIDATED §8b]

2. Eisenstein M. Can biology move into the matrix? *Nature*. 2026;654:286-288. doi: see PDF footnote ref 4 (verify final DOI; the document header cites doi:10.1038/d41586-2026-02777-8, verify).

3. Xing E, Song L. A world model of the virtual cell. GenBio AI technical report, May 3, 2026. No arXiv or DOI in document, verify.

4. Chuai G, Chen X, Yang X, et al. Towards building a world model to simulate perturbation-induced cellular dynamics by AlphaCell. *bioRxiv*. 2026. doi:10.64898/2026.03.02.709176.

5. Dong M, Adduri A, Gautam D, et al. STACK: in-context learning of single-cell biology. *bioRxiv*. 2026. doi:10.64898/2026.01.09.698608.

6. Wang C, Karimzadeh M, Ravindra NG, et al. X-Cell: scaling causal perturbation prediction across diverse cellular contexts via diffusion language models. *bioRxiv*. 2026. doi:10.64898/2026.03.18.712807.

---

### Single-cell foundation models

7. Cui H, Wang C, Maan H, et al. scGPT: toward building a foundation model for single-cell multi-omics using generative AI. *Nat Methods*. 2024. (Verify: full citation details and DOI not confirmed in source documents.)

8. Theodoris CV, Xiao L, Bhatt P, et al. Transfer learning enables predictions in network biology. *Nature*. 2023;618(7965):616-624. doi:10.1038/s41586-023-06139-9. [Geneformer]

9. Hao M, Gong J, Zeng X, et al. Large-scale foundation model on single-cell transcriptomics. *Nat Methods*. 2024;21:1481-1491. doi:10.1038/s41592-024-02305-7. [scFoundation] (verify)

10. Adduri A, Dong M, et al. STATE: a foundation model for single-cell perturbation prediction. 2025. (Verify: arXiv ID and journal/conference; cited as "Arc STATE" in source documents; no DOI confirmed.)

---

### Perturbation predictors

11. Roohani Y, Huang K, Leskovec J. GEARS: predicting transcriptional outcomes of novel multigene perturbations. *Nat Biotechnol*. 2024;42:216-228. doi:10.1038/s41587-023-01905-6.

12. Lotfollahi M, Wolf FA, Theis FJ. scGen predicts single-cell perturbation responses. *Nat Methods*. 2019;16(8):715-721. doi:10.1038/s41592-019-0494-8.

13. Lotfollahi M, Klimovskaia Susmelj A, De Donno C, et al. Predicting cellular responses to complex perturbations in high-throughput screens. *Mol Syst Biol*. 2023;19(6):e11517. doi:10.15252/msb.202211517. [CPA]

---

### Causal sVAE lineage and mechanism-sparsity models

14. Lachapelle S, Rodriguez Lopez P, Sharma Y, Everett K, Le Priol R, Lacoste A, Lacoste-Julien S. Disentanglement via mechanism sparsity regularization: a new principle for nonlinear ICA. *Proceedings of Machine Learning Research* 140:1-57. CLeaR 2022. arXiv:2107.10098.

15. Lopez R, Tagasovska N, Ra S, Cho K, Pritchard JK, Regev A. Learning causal representations of single cells via sparse mechanism shift modeling (sVAE+). CLeaR 2023. *Proceedings of Machine Learning Research*. arXiv:2211.03553. [FLAGGED: sVAE+ Lopez et al. arXiv:2211.03553 cited as CLeaR 2023 in source documents; verify conference proceedings year and volume, flagged unverified in SCIENCE_BRIEF.md]

16. Bereket M, Karaletsos T. Modelling cellular perturbations with the sparse additive mechanism shift variational autoencoder (SAMS-VAE). NeurIPS 2023. arXiv:2311.02794.

17. Hediyeh-zadeh S, Fischer T, Theis FJ. Disentanglement via mechanism sparsity by replaying realizations of the past (sVAE-ligr). ICLR 2024 MLG workshop. No arXiv ID in source document, verify.

18. Zhang J, Greenewald K, Squires C, Srivastava A, Shanmugam K, Uhler C. Identifiability guarantees for causal disentanglement from soft interventions. NeurIPS 2023. arXiv:2307.06250. [NOTE: arXiv ID 2307.06250 is from the full_proposal reference list; SCIENCE_BRIEF.md says "ID not in PDF, verify." The full_proposal entry is the more complete citation; confirm match.]

19. de la Fuente J, Lehmann R, Ruiz-Arenas C, et al. Interpretable causal representation learning for biological data in the pathway space (SENA-discrepancy-VAE). ICLR 2025. arXiv:2506.12439. [NOTE: arXiv ID 2506.12439 may postdate the ICLR 2025 submission date, verify arXiv ID and ICLR proceedings entry]

20. Schölkopf B, Locatello F, Bauer S, et al. Toward causal representation learning. *Proceedings of the IEEE*. 2021;109(5):612-634. doi:10.1109/JPROC.2021.3058954. [sparse mechanism shift hypothesis]

---

### Flow-based generative models

21. Palma A, Richter T, Zhang H, Dittadi A, Theis FJ. CellFlow: a generative flow-based model for single-cell count data. ICLR 2024 MLG workshop. No arXiv ID or DOI in source document, verify.

---

### Our team's perturbation model (internal)

22. [internal, embargoed] Team perturbation-model manuscript, anonymous submission to NeurIPS 2026, under review. Method name and title withheld; cited only in restricted section 32. Do not list in external reference sets.

---

### Sequence-to-regulatory / genomic grammar models

23. Avsec Z, et al. (Google DeepMind). AlphaGenome. GitHub: github.com/google-deepmind/alphagenome. Apache-2.0 code; noncommercial weights. 2025. [NOTE: author list and year disputed between source documents, full_proposal cites "Avsec Z, et al. / Google DeepMind (2025)" while an earlier draft cited "Outeiral C, Strahm M, Shi J, et al. (2021; updated)." Verify the correct citation, flagged in PRIOR_WORK_CONSOLIDATED §8c]

24. Avsec Z, Agarwal V, Visentin D, et al. Effective gene expression prediction from sequence by integrating long-range interactions. *Nat Methods*. 2021;18(10):1196-1203. doi:10.1038/s41592-021-01252-x. [Enformer]

25. Linder J, Bhate A, Rajesh A, et al. Borzoi: sequence modeling of gene expression at enhancer resolution. *Nat Genet*. 2023. (Verify: DOI and volume/pages not confirmed in source documents.)

---

### Intervention-design GNNs

26. Gonzalez G, Lin X, Herath I, Veselkov K, Bronstein M, Zitnik M. Combinatorial prediction of therapeutic perturbations using causally inspired neural networks (PDGrapher). *Nat Biomed Eng*. 2025. doi:10.1038/s41551-025-01481-x.

---

### Systems-biology and network tools

27. Liu A, Trairatphisan P, Gjerga E, Didangelos A, Barratt J, Saez-Rodriguez J. From expression footprints to causal pathways: contextualizing large signaling networks with CARNIVAL. *NPJ Syst Biol Appl*. 2019;5:40. doi:10.1038/s41540-019-0118-z.

28. Dugourd A, Kuppe C, Sciacovelli M, et al. Causal integration of multi-omics data with prior knowledge to generate mechanistic hypotheses (COSMOS). *Mol Syst Biol*. 2021;17(1):e9730. doi:10.15252/msb.20209730.

29. Browaeys R, Saelens W, Saeys Y. NicheNet: modeling intercellular communication by linking ligands to target genes. *Nat Methods*. 2020;17(2):159-162. doi:10.1038/s41592-019-0667-5.

30. Virtual Brain Twin Consortium. virtualbraintwin.eu. 2025. (Consortium reference; no single DOI; cite website and relevant publications.)

---

### Network and co-expression tools

31. Su Y, Miller R, Hazelbaker B, et al. Cell-type-specific co-expression inference from single-cell RNA-sequencing data (CS-CORE). *Nat Commun*. 2023;14:4846. doi:10.1038/s41467-023-40503-7.

32. Song D, Wang Q, Yan G, et al. scDesign3 generates realistic in silico single-cell and spatial omics data using statistical copula models. *Nat Biotechnol*. 2024;42:247-252. doi:10.1038/s41587-023-01772-1.

33. Garrido-Rodriguez M, Holland CH, Ramirez Flores RO, et al. Integrating knowledge and omics via large-scale models of signaling networks (OmniPath). *Mol Syst Biol*. 2022;18:e11036. doi:10.15252/msb.202211036.

---

### Neuro-specific network priors

34. Lage K, et al. A cell-type-resolved interactome of autism risk genes (IGF2BP1-3 complex; AP-MS in iNs). *Cell Genomics*. 2022;2(9):100182. doi:10.1016/j.xgen.2022.100182.

35. Emani PS, Liu JJ, Clarke D, et al. Single-cell genomics and regulatory networks for 388 human brains (PsychENCODE brainSCOPE). *Science*. 2024;384(6698):eadi5199. doi:10.1126/science.adi5199.

---

### Ontology and embedding tools

36. Xiong B, Cochez M, Nayyeri M, Staab S. TransBox: EL++-closed ontology embedding with box embeddings. arXiv:2410.14571. 2024.

---

### Polygenic risk score precedent

37. Choi SW, Mak TSH, O'Reilly PF. Tutorial: a guide to performing polygenic risk score analyses. *Nat Protoc*. 2020;15(9):2759-2772. doi:10.1038/s41596-020-0353-1. [PRSet / PRSice-2 pathway-based polygenic scores; precedent for our proprietary pathway factorization]

---

### PI-authored papers and clinical datasets

38. Ruzicka WB, Mohammadi S, Fullard JF, et al. Single-cell multi-cohort dissection of the schizophrenia transcriptome. *Science*. 2024;384(6698):eadg5136. doi:10.1126/science.adg5136.

39. Batiuk MY, Tyler T, Dragicevic K, et al. Upper-layer cortical neurons drive schizophrenia-associated pathology in organoids (PsychAD). *Nat Neurosci*. 2024;27:1773-1784. doi:10.1038/s41593-024-01648-8. (verify DOI)

40. Mathys H, Davila-Velderrain J, Peng Z, et al. Single-cell transcriptomic analysis of Alzheimer's disease. *Nature*. 2019;570(7761):332-337. doi:10.1038/s41586-019-1195-2.

---

### Genetics of schizophrenia and 22q11DS

41. Trubetskoy V, Pardinas AF, Qi T, et al. Mapping genomic loci implicates genes and synaptic biology in schizophrenia (PGC). *Nature*. 2022;604(7906):502-508. doi:10.1038/s41586-022-04434-5.

42. Singh T, Poterba T, Curtis D, et al. Rare coding variants in ten genes confer substantial risk for schizophrenia (SCHEMA). *Nature*. 2022;604(7906):509-516. doi:10.1038/s41586-022-04556-w.

43. Schneider M, Debbané M, Bassett AS, et al. Psychiatric disorders from childhood to adulthood in 22q11.2 deletion syndrome: results from the International Consortium on Brain and Behavior in 22q11.2 Deletion Syndrome. *Am J Psychiatry*. 2014. [Meta-analysis cited at PMID:36786112, verify: the PMID cited in PRIOR_WORK_CONSOLIDATED is Schneider M et al. 2023 BJPsych; confirm correct PMID, journal, and year for the 11.5% pooled psychosis prevalence figure.]

44. Murphy KC, Jones LA, Owen MJ. High rates of schizophrenia in adults with velo-cardio-facial syndrome. *Arch Gen Psychiatry*. 1999;56(10):940-945. PMID:10199234.

45. Paylor R, Glaser B, Mupo A, et al. Tbx1 haploinsufficiency is linked to behavioral disorders in mice and humans: implications for 22q11 deletion syndrome. *Proc Natl Acad Sci USA*. 2006;103(20):7729-7734. PMID:16684884. doi:10.1073/pnas.0600206103.

46. Funke B, Epstein JA, Kochilas LK, et al. Mice overexpressing genes from the 22q11 region deleted in velo-cardio-facial syndrome/DiGeorge syndrome have middle and inner ear defects. *Hum Mol Genet*. 2001. [NOTE: PRIOR_WORK_CONSOLIDATED cites Funke B et al. 2007 Mol Med PMID:17622321 as evidence against TBX1 in nonsyndromic psychosis; confirm which Funke et al. paper is intended.]

47. Vorstman JAS, Breetvelt EJ, Duijff SN, et al. Cognitive decline preceding the onset of psychosis in patients with 22q11.2 deletion syndrome. *JAMA Psychiatry*. 2015. [Vorstman 2017 Nat Neurosci cited in source, verify: PRIOR_WORK_CONSOLIDATED cites PMID:28379838 as Vorstman JAS et al. 2017 Nat Neurosci; confirm journal, year, and DOI.]

48. Nair A, et al. 22q11.2 deletion syndrome shapes brain transcriptome and regional cell-type signatures. *Mol Psychiatry*. 2024;29. doi: (verify). PMID: (verify). [Page numbers absent in all source documents; flagged in PRIOR_WORK_CONSOLIDATED §8d]

49. Kim Y, Bhatt DK. TBX1 in oligodendrocyte lineage specifically disrupts myelination of fimbria axons. *bioRxiv*. 2025. doi: see bioRxiv 2025.12.30.697076.

---

### Agentic science and orchestration systems

50. Gottweis J, et al. (Google DeepMind). Towards an AI co-scientist. *Nature*. 2025. (Verify: conference or journal; cited as "Co-Scientist, Nature 2026" and "Google Labs/Cloud" in source documents; confirm correct venue and year.)

51. Lu C, Lu C, Lange RT, et al. The AI Scientist: towards fully automated open-ended scientific discovery. Sakana AI. 2024. arXiv:2408.06292.

52. Wei C, Huang K, et al. Biomni: a capable generalist biomedical AI agent. Stanford/Phylo. 2025. (Verify: arXiv ID or preprint DOI; cited as "Biomni (Stanford; Phylo 2025)" in source documents.)

53. Boiko DA, MacKnight R, Kline B, Gomes G. Autonomous chemical research with large language models (Coscientist). *Nature*. 2023;624(7992):570-578. doi:10.1038/s41586-023-06792-0.

54. Swanson K, Wu T, Bulaong NL, et al. The Virtual Lab: AI agents design new SARS-CoV-2 nanobodies with experimental validation. *Nat Biomed Eng*. 2025. doi: (verify). arXiv:2408.09618.

55. Ghafarollahi A, Buehler MJ. SciAgents: automating scientific discovery through multi-agent intelligent graph reasoning. arXiv:2409.05556. 2024.

56. LLNL. Open AI Co-Scientist (open reimplementation). github.com/llnl/open-ai-co-scientist. 2024.

---

### Validation and phenomics (TA4)

57. Tegtmeyer M, Liyanage D, Han Y, et al. Combining phenomics with transcriptomics reveals cell-type-specific morphological and molecular signatures of the 22q11.2 deletion (NeuroPainting). *Nat Commun*. 2025;16(1):6332. doi:10.1038/s41467-025-61547-x.

58. Haghighi M, et al. Identifying and targeting abnormal mitochondrial localization associated with psychosis. *bioRxiv*. 2025. doi: see bioRxiv 2025.10.08.676630.

59. Replogle JM, Saunders RA, Pogson AN, et al. Mapping information-rich genotype-phenotype landscapes with genome-scale Perturb-seq. *Cell*. 2022;185(19):3615-3632. doi:10.1016/j.cell.2022.05.013. [NOTE: PRIOR_WORK_CONSOLIDATED §8e flags an authorship attribution issue between Replogle and Zheng author lists; confirm Replogle et al. as first author of Cell 185:19 3615-3632.]

---

### Open Targets and drug target validation

60. Minikel EV, Painter JL, Dong CC, Nelson MR. Refining the impact of genetic evidence on clinical success. *Nature*. 2024;629(8012):624-629. doi:10.1038/s41586-024-07316-0.

61. Falaguera MJ, McDonagh EM, Ochoa D, et al. Temporal trends in evidence supporting novel drug target discovery (Open Targets). *Nat Commun*. 2025;17(1):492. doi:10.1038/s41467-025-67180-y.

62. Ochoa D, Hercules A, Carmona M, et al. The next-generation Open Targets Platform. *Nucleic Acids Res*. 2023;51(D1):D1353-D1359. doi:10.1093/nar/gkac1046.

63. Mountjoy E, Schmidt EM, Carmona M, et al. An open approach to systematically prioritize causal variants and genes at GWAS loci (Locus-to-Gene). *Nat Genet*. 2021;53:1527-1533. doi:10.1038/s41588-021-00945-5.

---

### Reproducibility and knowledge infrastructure

64. Xu J, Yu C, Xu J, et al. PubMed knowledge graph 2.0: connecting papers, patents, and clinical trials in biomedical science. *Sci Data*. 2025;12:1018. doi:10.1038/s41597-025-05343-8.

65. Nelson MR, Tipney H, Painter JL, et al. The support of human genetic evidence for approved drug indications. *Nat Genet*. 2015;47(8):856-860. doi:10.1038/ng.3314.

---

### Clinical NLP and hypothesis-grounding tools

66. Neumann M, King D, Beltagy I, Ammar W. ScispaCy: fast and robust models for biomedical natural language processing. arXiv:1902.07669. 2019.

67. Chamberlin C, et al. medspaCy: a spaCy-based framework for clinical NLP. *AMIA*. 2021. (Verify: full citation and proceedings reference.)

---

### ARPA-H solicitation

68. ARPA-H. Intelligent Generator of Research (IGoR) Innovative Solutions Opening. ARPA-H-SOL-26-155. 2026. sam.gov opportunity 287ec68e.

---

### Verification flags (pre-submission checklist)

Items requiring independent verification before the Aug 6 full proposal:

- **[Flag 1] Bunne et al. Cell volume.** Source documents disagree between Cell 187(25):7045-7063 (SCIENCE_BRIEF) and Cell 189(7):1175-1188 (earlier SS draft). The SCIENCE_BRIEF.md cite (187:7045-7063, doi:10.1016/j.cell.2024.11.015) matches the DOI content; confirm final published volume and page range.

- **[Flag 2] sVAE+ Lopez et al. arXiv:2211.03553.** SCIENCE_BRIEF.md notes this was published at CLeaR 2023 (second conference on Causal Learning and Reasoning, PMLR). Confirm PMLR volume number and proceedings pages; citation currently listed as "PMLR" without volume.

- **[Flag 3] AlphaGenome author list and year.** Two source documents give conflicting author lists (Avsec Z et al. 2025 vs. Outeiral C et al. 2021). These may refer to different versions or different papers. Verify the correct citation for the 2025/2026 AlphaGenome tool used in our pipeline.

- **[Flag 4] Bunne et al. in State (Arc) comparators.** The Eisenstein Nature 2026 article cites "State" (Arc Institute) and lists its volume/pages differently in different sources. Confirm the full State citation (Adduri et al., arXiv ID, and any conference proceedings).

- **[Flag 5] Zhang et al. NeurIPS 2023 arXiv:2307.06250.** The SCIENCE_BRIEF.md says "ID not in PDF, verify." The full_proposal reference list gives arXiv:2307.06250. Confirm this arXiv ID resolves to the Zhang, Greenewald, Squires, Srivastava, Shanmugam, Uhler paper.

- **[Flag 6] SENA-discrepancy-VAE arXiv:2506.12439.** The arXiv ID 2506.12439 has a date prefix (2506 = June 2025 or June 2026) that may postdate the ICLR 2025 submission; verify the arXiv ID and confirm the paper's ICLR 2025 acceptance.

- **[Flag 7] Schneider et al. BJPsych 2023 PMID:36786112.** Confirm journal name (*BJPsych* = British Journal of Psychiatry), year (2023), and the 11.5% pooled psychosis prevalence figure as the cited statistic.

- **[Flag 8] Nair et al. Mol Psychiatry 2024 vol. 29.** Page numbers absent in all source documents. Confirm volume, issue, pages, and PMID/DOI.

- **[Flag 9] State (Arc STATE) full citation.** Cited as "Adduri et al. 2025" in source documents without arXiv ID, journal, or conference. Obtain full citation.

- **[Flag 10] CellFlow ICLR 2024 MLG workshop.** No arXiv ID or DOI in source documents. Confirm preprint or proceedings reference.

- **[Flag 11] sVAE-ligr ICLR 2024 MLG workshop.** No arXiv ID or DOI in source documents. Confirm preprint or proceedings reference.

- **[Flag 12] PKG 2.0 / PubMed Knowledge Graph.** Source documents cite "PKG25S4 not yet published" in some contexts and cite Xu et al. Sci Data 2025 in others. Confirm which version of the PubMed Knowledge Graph is live and citable; reference 64 above is the Sci Data 2025 entry.

- **[Flag 13] Replogle et al. authorship.** Confirm that Cell 185(19):3615-3632 is Replogle as first author, not Zheng GXY (a different Perturb-seq paper from a different year). See PRIOR_WORK_CONSOLIDATED §8e.

- **[Flag 14] Vorstman et al. 2017 Nat Neurosci PMID:28379838.** Confirm journal (Nat Neurosci vs. JAMA Psychiatry) and full citation details.

- **[Flag 15] Funke B et al. 2007 Mol Med PMID:17622321.** Confirm full citation; note this is the "against" evidence that TBX1 sequence variation does not contribute to nonsyndromic psychosis.

- **[Flag 16] Life Sci Alliance 8(2):e202403075 (TBX1 vitamin B12 rescue).** Referenced in PRIOR_WORK_CONSOLIDATED §2d as a "mouse rescue" reference for the TBX1 mouse-rescue phenotype. Confirm full citation and add to references before submission.

- **[Flag 17] Biomni Phylo preprint.** No arXiv ID or DOI confirmed. Obtain preprint reference before citing in the proposal.


## Standards and frameworks (added 2026-06-14, from the standards-comparison reviews)

Model and simulation: SBML L3V2 Core and packages (qual, fbc, comp, multi, spatial); CellML 2.0 (doi:10.15252/msb.20199110); SED-ML L1V5 (PMID:38613325); SBGN PD L1V2.1; NeuroML v2.3 (PMC11723582); OMEX/COMBINE archive (PMC4272562); whole-cell modeling and Vivarium (PMID:35134830; Karr et al. 2012).
Executable disease knowledge: Disease Maps and MINERVA (bioRxiv 2024.08.28.610042); CaSQ (PMC7575051); MaBoSS/CoLoMoTo; COVID-19 Disease Map (FAIRDOMHub model 714); WikiPathways GPML2021; Reactome.
Causal-knowledge standards: BioPAX L3 (PMC11585474); BEL/CBN (PMC4401337); GO-CAM (Nat Genet 2019, PMC7012280); INDRA, CoGEx, EMMAA (Gyori Lab).
Semantic backbone: MIRIAM (PMC2259379); SBO; Relation Ontology; Biolink Model (arXiv:2203.13906); OBO Foundry (GO, CL, UBERON, MONDO 2025, HPO).
Knowledge graphs: Monarch 2024 (NAR D938); Open Targets 25.03 (L2G, GWAS fine-mapping); PrimeKG (doi:10.1038/s41597-023-01960-3); SPOKE; Hetionet; Clinical Knowledge Graph.
Temporal/progression: SuStaIn (PMC8387598); Event-Based Model (arXiv:2512.03467); pseudotime/CellRank 2.
Knowledge-omics bridge: P-NET (PMC8514339); KPNN (Genome Biol 2020); VEGA (doi:10.1038/s41467-021-26017-0); SENA-discrepancy-VAE (arXiv:2506.12439); GEARS (PMC11180609); AnnData/CZ CELLxGENE Census (NAR 2025, D886).


## Disease genetics: penetrant schizophrenia, 22q11DS, TBX1 (added 2026-06-14)

22q11DS and schizophrenia: Murphy et al. 1999 (PMID:10199234); Karayiorgou et al. 1994 (PMID:8213821), 1995 (PMID:7667299); Gothelf et al. 2007 (PMID:17046719); Schneider et al. 2023 (PMID:36786112); Vorstman et al. 2017 (PMID:28379838); Fiksinski et al. 2022 (PMID:35577927); Malone et al. 2022 (doi:10.1038/s41380-022-01674-9).
TBX1: Paylor et al. 2006 (PMID:16684884); Funke et al. 2007 (PMID:17622321); Vitelli et al. 2017 (PMID:27131548); Kim and Bhatt 2025 (bioRxiv 2025.12.30.697076); Stark et al. 2008 (IJNP); Kim et al. 2023 (PMC10350205).
Rare variants and loci: SCHEMA, Singh et al. 2022 (PMID:35396579); OMIM SCZD1 to SCZD19; MONDO:0005090 and MONDO:0011511 (OLS4). Selected SCZD-gene primary refs: DISC1 Millar 2000 (PMID:10767314); CHRNA7 Stefansson 2008 (PMID:18568025); SHANK3 Gauthier 2010 (PMID:20694004); VIPR2 Vacic 2011 (PMID:21346763); NRXN1 Rujescu 2009 (PMID:19059627); SLC1A1 Myles-Worsley 2013 (PMID:23606419); RBM12 Hoeffding 2017 (PMID:28678325).
