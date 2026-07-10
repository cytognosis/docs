# NER

> **Status**: Active
> **Date**: 2026-07-10
> **Author**: @shahin
> **Audience**: engineers
> **Tags**: `engineering`
> **Variants**: Technical (this doc) - Readable (Obsidian twin optional, same filename) - Agent (n/a)

## spaCy, scispacy



## [medspaCy](https://github.com/medspacy/medspacy)

MedSpaCy is a library of tools for performing clinical NLP and text processing tasks with the popular [spaCy](https://spacy.io) 
framework. The `medspacy` package brings together a number of other packages, each of which implements specific 
functionality for common clinical text processing specific to the clinical domain, such as sentence segmentation, 
contextual analysis and attribute assertion, and section detection.

`medspacy` is modularized so that each component can be used independently. All of `medspacy` is designed to be used 
as part of a `spacy` processing pipeline. Each of the following modules is available as part of `medspacy`:
- `medspacy.preprocess`: Destructive preprocessing for modifying clinical text before processing
- `medspacy.sentence_splitter`: Clinical sentence segmentation
- `medspacy.ner`: Utilities for extracting concepts from clinical text
- `medspacy.context`: Implementation of the [ConText](https://www.sciencedirect.com/science/article/pii/S1532046409000744)
algorithm for detecting semantic modifiers and attributes of entities, including negation and uncertainty.
- `medspacy.section_detection`: Clinical section detection and segmentation
- `medspacy.postprocess`: Flexible framework for modifying and removing extracted entities
- `medspacy.io`: Utilities for converting processed texts to structured data and interacting with databases
- `medspacy.visualization`: Utilities for visualizing concepts and relationships extracted from text
- `SpacyQuickUMLS`: UMLS concept extraction compatible with spacy and medspacy implemented by [our fork](https://github.com/medspacy/QuickUMLS) of [QuickUMLS](https://github.com/Georgetown-IR-Lab/QuickUMLS). More detail on this component, how to use it, how to generate UMLS resources beyond the small UMLS sample can be found in [this notebook](notebooks/11a-QuickUMLS_Extraction_Defaults.ipynb).

Future work will include I/O, relations extraction, and pre-trained clinical models.



The [parent repo](https://github.com/medspacy,) also includes also many other tools, including:

* https://github.com/medspacy/medspacy_io: A collection of modules to facilitate reading text from various sources and writing to various sources.
* https://github.com/medspacy/medspacyV: The medspacyV is a desktop application developed by the Mayo Clinic's Center for Clinical and Translational Science (CCaTS) Informatics Team. It offers a visual interface for the open-source medspacy library.
* https://github.com/medspacy/PyRuSH: PyRuSH is the python implementation of RuSH (Ru le-based sentence S egmenter using H ashing), which is originally developed using Java. RuSH is an efficient, reliable, and easy adaptable rule-based sentence segmentation solution. It is specifically designed to handle the telegraphic written text in clinical note. It leverages a nested hash table to execute simultaneous rule processing, which reduces the impact of the rule-base growth on execution time and eliminates the effect of rule order on accuracy.
* https://github.com/medspacy/QuickUMLS: System for Medical Concept Extraction. QuickUMLS (Soldaini and Goharian, 2016) is a tool for fast, unsupervised biomedical concept extraction from medical text. It takes advantage of Simstring (Okazaki and Tsujii, 2010) for approximate string matching. For more details on how QuickUMLS works, we remand to our paper.
