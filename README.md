# Awesome Graph Neural Network Systems [![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)

A list of awesome systems for graph neural network (GNN). If you have any comment, please create an issue or pull request.

## Open Source Libraries

- [PyG: Graph Neural Network Library for PyTorch](https://github.com/rusty1s/pytorch_geometric) ![GitHub stars](https://img.shields.io/github/stars/rusty1s/pytorch_geometric.svg?logo=github&label=Stars)

- [DGL: Python Package Built to Ease Deep Learning on Graph](https://github.com/dmlc/dgl) ![GitHub stars](https://img.shields.io/github/stars/dmlc/dgl.svg?logo=github&label=Stars)

- [Graph Nets: Build Graph Nets in Tensorflow](https://github.com/deepmind/graph_nets) ![GitHub stars](https://img.shields.io/github/stars/deepmind/graph_nets.svg?logo=github&label=Stars)

- [Euler: A Distributed Graph Deep Learning Framework](https://github.com/alibaba/euler) ![GitHub stars](https://img.shields.io/github/stars/alibaba/euler.svg?logo=github&label=Stars)

- [StellarGraph: Machine Learning on Graphs](https://github.com/stellargraph/stellargraph) ![GitHub stars](https://img.shields.io/github/stars/stellargraph/stellargraph.svg?logo=github&label=Stars)

- [Spektral: Graph Neural Networks with Keras and Tensorflow 2](https://github.com/danielegrattarola/spektral) ![GitHub stars](https://img.shields.io/github/stars/danielegrattarola/spektral.svg?logo=github&label=Stars)

- [PGL: An Efficient and Flexible Graph Learning Framework Based on PaddlePaddle](https://github.com/PaddlePaddle/PGL) ![GitHub stars](https://img.shields.io/github/stars/PaddlePaddle/PGL.svg?logo=github&label=Stars)

- [CogDL: An Extensive Toolkit for Deep Learning on Graphs](https://github.com/THUDM/cogdl) ![GitHub stars](https://img.shields.io/github/stars/THUDM/cogdl.svg?logo=github&label=Stars)

- [DIG: A Turnkey Library for Diving into Graph Deep Learning Research](https://github.com/divelab/DIG) ![GitHub stars](https://img.shields.io/github/stars/divelab/DIG.svg?logo=github&label=Stars)

- [Graph-Learn: An Industrial Graph Neural Network Framework](https://github.com/alibaba/graph-learn) ![GitHub stars](https://img.shields.io/github/stars/alibaba/graph-learn.svg?logo=github&label=Stars)

- [Jraph: A Graph Neural Network Library in Jax](https://github.com/deepmind/jraph) ![GitHub stars](https://img.shields.io/github/stars/deepmind/jraph.svg?logo=github&label=Stars)

## Papers

### Survey Papers

- **[arXiv 2022]** Parallel and Distributed Graph Neural Networks: An In-Depth Concurrency Analysis (*ETHZ*) [[paper]](https://arxiv.org/abs/2205.09702)
- **[CSUR 2022]** Computing Graph Neural Networks: A Survey from Algorithms to Accelerators (*UPC*) [[paper]](https://dl.acm.org/doi/10.1145/3477141)

### Libraries
- **[JMLR 2021]** DIG: A Turnkey Library for Diving into Graph Deep Learning Research (*TAMU*) [[paper]](https://arxiv.org/abs/2103.12608) [[code]](https://github.com/divelab/DIG)
- **[arXiv 2021]** CogDL: A Toolkit for Deep Learning on Graphs (*THU*) [[paper]](https://arxiv.org/abs/2103.00959) [[code]](https://github.com/THUDM/cogdl)
- **[CIM 2021]** Graph Neural Networks in TensorFlow and Keras with Spektral (*Università della Svizzera italiana*) [[paper]](https://arxiv.org/abs/2006.12138) [[code]](https://github.com/danielegrattarola/spektral)
- **[arXiv 2019]** Deep Graph Library: A Graph-Centric, Highly-Performant Package for Graph Neural Networks (*AWS*) [[paper]](https://arxiv.org/abs/1909.01315v2) [[code]](https://github.com/dmlc/dgl)
- **[VLDB 2019]** AliGraph: A Comprehensive Graph Neural Network Platform (*Alibaba*) [[paper]](https://dl.acm.org/doi/pdf/10.14778/3352063.3352127) [[code]](https://github.com/alibaba/graph-learn)
- **[arXiv 2019]** Fast Graph Representation Learning with PyTorch Geometric (*TU Dortmund University*) [[paper]](https://arxiv.org/abs/1903.02428) [[code]](https://github.com/rusty1s/pytorch_geometric)
- **[arXiv 2018]** Relational Inductive Biases, Deep Learning, and Graph Networks (*DeepMind*) [[paper]](https://arxiv.org/abs/1806.01261) [[code]](https://github.com/deepmind/graph_nets)

### GNN Compilers

- **[MLSys 2022]** Graphiler: Optimizing Graph Neural Networks with Message Passing Data Flow Graph (*ShanghaiTech*) [[paper]](https://proceedings.mlsys.org/paper/2022/file/a87ff679a2f3e71d9181a67b7542122c-Paper.pdf) [[code]](https://github.com/xiezhq-hermann/graphiler)
- **[MLSys 2022]** Understanding GNN Computational Graph: A Coordinated Computation, IO, and Memory Perspective (*THU*) [[paper]](https://proceedings.mlsys.org/paper/2022/file/9a1158154dfa42caddbd0694a4e9bdc8-Paper.pdf) [[code]](https://github.com/dgSPARSE/dgNN)
- **[HPDC 2022]** TLPGNN: A Lightweight Two-Level Parallelism Paradigm for Graph Neural Network Computation on GPU (*GW*) [[paper]](https://dl.acm.org/doi/abs/10.1145/3502181.3531467)
- **[EuroSys 2022]** GNNLab: A Factored System for Sample-based GNN Training over GPUs (*SJTU*) [[paper]](https://dl.acm.org/doi/abs/10.1145/3492321.3519557) [[code]](https://github.com/SJTU-IPADS/gnnlab)
- **[VLDB 2021]** Large Graph Convolutional Network Training with GPU-Oriented Data Communication Architecture (*UIUC*) [[paper]](https://arxiv.org/abs/2103.03330) [[code]](https://github.com/K-Wu/pytorch-direct_dgl)
- **[IPDPS 2021]** FusedMM: A Unified SDDMM-SpMM Kernel for Graph Embedding and Graph Neural Networks (*Indiana University Bloomington*) [[paper]](https://arxiv.org/abs/2011.06391) [[code]](https://github.com/HipGraph/FusedMM)
- **[EuroSys 2021]** Seastar: Vertex-Centric Programming for Graph Neural Networks (*CUHK*) [[paper]](http://www.cse.cuhk.edu.hk/~jcheng/papers/seastar_eurosys21.pdf)
- **[PPoPP 2021]** Understanding and Bridging the Gaps in Current GNN Performance Optimizations (*THU*) [[paper]](https://dl.acm.org/doi/pdf/10.1145/3437801.3441585) [[code]](https://github.com/xxcclong/GNN-Computing)
- **[SC 2020]** FeatGraph: A Flexible and Efficient Backend for Graph Neural Network Systems (*Cornell*) [[paper]](https://arxiv.org/pdf/2008.11359.pdf) [[code]](https://github.com/dglai/FeatGraph)
- **[SC 2020]** GE-SpMM: General-purpose Sparse Matrix-Matrix Multiplication on GPUs for Graph Neural Networks (*THU*) [[paper]](https://arxiv.org/abs/2007.03179) [[code]](https://github.com/hgyhungry/ge-spmm)
- **[ICCAD 2020]** fuseGNN: Accelerating Graph Convolutional Neural Network Training on GPGPU (*UCSB*) [[paper]](https://seal.ece.ucsb.edu/sites/default/files/publications/fusegcn_camera_ready_.pdf) [[code]](https://github.com/apuaaChen/gcnLib)
- **[IPDPS 2020]** PCGCN: Partition-Centric Processing for Accelerating Graph Convolutional Network (*PKU*) [[paper]](https://ieeexplore.ieee.org/document/9139807)

### Distributed GNN Training Systems

- **[MLSys 2022]** BNS-GCN: Efficient Full-Graph Training of Graph Convolutional Networks with Partition-Parallelism and Random Boundary Node Sampling (*Rice, UIUC*) [[paper]](https://proceedings.mlsys.org/paper/2022/file/d1fe173d08e959397adf34b1d77e88d7-Paper.pdf) [[code]](https://github.com/RICE-EIC/BNS-GCN)
- **[MLSys 2022]** Sequential Aggregation and Rematerialization: Distributed Full-batch Training of Graph Neural Networks on Large Graphs (*Intel*) [[paper]](https://arxiv.org/abs/2111.06483) [[code]](https://github.com/IntelLabs/SAR)
- **[WWW 2022]** PaSca: A Graph Neural Architecture Search System under the Scalable Paradigm (*PKU*) [[paper]](https://dl.acm.org/doi/abs/10.1145/3485447.3511986)
- **[ICLR 2022]** PipeGCN: Efficient Full-Graph Training of Graph Convolutional Networks with Pipelined Feature Communication (*Rice*) [[paper]](https://openreview.net/pdf?id=kSwqMH0zn1F) [[code]](https://github.com/RICE-EIC/PipeGCN)
- **[ICLR 2022]** Learn Locally, Correct Globally: A Distributed Algorithm for Training Graph Neural Networks (*PSU*) [[paper]](https://openreview.net/pdf?id=FndDxSz3LxQ) [[code]](https://github.com/MortezaRamezani/llcg)
- **[arXiv 2021]** Distributed Hybrid CPU and GPU training for Graph Neural Networks on Billion-Scale Graphs (*AWS*) [[paper]](https://arxiv.org/pdf/2112.15345.pdf)
- **[SC 2021]** DistGNN: Scalable Distributed Training for Large-Scale Graph Neural Networks (*Intel*) [[paper]](https://dl.acm.org/doi/pdf/10.1145/3458817.3480856) [[code]](https://github.com/dmlc/dgl/pull/3024)
- **[SC 2021]** Efficient Scaling of Dynamic Graph Neural Networks (*IBM*) [[paper]](https://dl.acm.org/doi/pdf/10.1145/3458817.3480858)
- **[CLUSTER 2021]** 2PGraph: Accelerating GNN Training over Large Graphs on GPU Clusters (*NUDT*) [[paper]](https://ieeexplore.ieee.org/abstract/document/9556026)
- **[OSDI 2021]** $P^3$: Distributed Deep Graph Learning at Scale (*MSR*) [[paper]](https://www.usenix.org/system/files/osdi21-gandhi.pdf)
- **[OSDI 2021]** Dorylus: Affordable, Scalable, and Accurate GNN Training with Distributed CPU Servers and Serverless Threads (*UCLA*) [[paper]](http://web.cs.ucla.edu/~harryxu/papers/dorylus-osdi21.pdf) [[code]](https://github.com/uclasystem/dorylus) 
- **[EuroSys 2021]** FlexGraph: A Flexible and Efficient Distributed Framework for GNN Training (*Alibaba*) [[paper]](https://dl.acm.org/doi/pdf/10.1145/3447786.3456229)
- **[EuroSys 2021]** DGCL: An Efficient Communication Library for Distributed GNN Training (*CUHK*) [[paper]](https://dl.acm.org/doi/abs/10.1145/3447786.3456233) [[code]](https://github.com/czkkkkkk/ragdoll)
- **[SC 2020]** Reducing Communication in Graph Neural Network Training (*UC Berkeley*) [[paper]](https://arxiv.org/pdf/2005.03300.pdf) [[code]](https://github.com/PASSIONLab/CAGNET)
- **[SoCC 2020]** PaGraph: Scaling GNN Training on Large Graphs via Computation-aware Caching (*USTC*) [[paper]](https://dl.acm.org/doi/pdf/10.1145/3419111.3421281) [[code]](https://github.com/zhiqi-0/PaGraph)
- **[VLDB 2020]** G$^3$: When Graph Neural Networks Meet Parallel Graph Processing Systems on GPUs (*NUS*) [[paper]](http://www.vldb.org/pvldb/vol13/p2813-liu.pdf) [[code]](https://github.com/Xtra-Computing/G3)
- **[IA3 2020]** DistDGL: Distributed Graph Neural Network Training for Billion-Scale Graphs (*AWS*) [[paper]](https://arxiv.org/pdf/2010.05337.pdf) [[code]](https://github.com/dmlc/dgl/tree/master/python/dgl/distributed)
- **[MLSys 2020]** Improving the Accuracy, Scalability, and Performance of Graph Neural Networks with Roc (*Stanford*) [[paper]](https://proceedings.mlsys.org/paper/2020/file/fe9fc289c3ff0af142b6d3bead98a923-Paper.pdf) [[code]](https://github.com/jiazhihao/ROC)
- **[arXiv 2020]** AGL: A Scalable System for Industrial-purpose Graph Machine Learning (*Ant Financial Services Group*) [[paper]](https://arxiv.org/abs/2003.02454)
- **[ATC 2019]** NeuGraph: Parallel Deep Neural Network Computation on Large Graphs (*PKU*) [[paper]](https://www.usenix.org/system/files/atc19-ma_0.pdf)

### Training Systems for Scaling Graphs

- **[ICML 2022]** GraphFM: Improving Large-Scale GNN Training via Feature Momentum (*TAMU*) [[paper]](https://arxiv.org/abs/2206.07161) [[code]](https://github.com/divelab/DIG/tree/dig/dig/lsgraph)
- **[ICML 2021]** GNNAutoScale: Scalable and Expressive Graph Neural Networks via Historical Embeddings (*TU Dortmund University*) [[paper]](https://arxiv.org/abs/2106.05609) [[code]](https://github.com/rusty1s/pyg_autoscale)
- **[OSDI 2021]** GNNAdvisor: An Adaptive and Efficient Runtime System for GNN Acceleration on GPUs (*UCSB*) [[paper]](https://www.usenix.org/system/files/osdi21-wang-yuke.pdf) [[code]](https://github.com/YukeWang96/OSDI21_AE)

### Quantized GNNs

- **[ICLR 2022]** EXACT: Scalable Graph Neural Networks Training via Extreme Activation Compression (*Rice*) [[paper]](https://openreview.net/pdf?id=vkaMaq95_rX) [[code]](https://github.com/warai-0toko/Exact)
- **[PPoPP 2022]** QGTC: Accelerating Quantized Graph Neural Networks via GPU Tensor Core (*UCSB*) [[paper]](https://arxiv.org/abs/2111.09547) [[code]](https://github.com/YukeWang96/PPoPP22_QGTC)
- **[CVPR 2021]** Binary Graph Neural Networks (*ICL*) [[paper]](https://arxiv.org/abs/2012.15823) [[code]](https://github.com/mbahri/binary_gnn)
- **[EuroMLSys 2021]** Learned Low Precision Graph Neural Networks (*Cambridge*) [[paper]](https://arxiv.org/abs/2009.09232)
- **[ICLR 2021]** Degree-Quant: Quantization-Aware Training for Graph Neural Networks (*Cambridge*) [[paper]](https://arxiv.org/abs/2008.05000) [[code]](https://github.com/camlsys/degree-quant)

### GNN Dataloaders

- **[MLSys 2022]** Accelerating Training and Inference of Graph Neural Networks with Fast Sampling and Pipelining (*MIT*) [[paper]](https://proceedings.mlsys.org/paper/2022/file/35f4a8d465e6e1edc05f3d8ab658c551-Paper.pdf) [[code]](https://github.com/MITIBMxGraph/SALIENT)
- **[TPDS 2021]** Efficient Data Loader for Fast Sampling-Based GNN Training on Large Graphs (*USTC*) [[paper]](https://gnnsys.github.io/papers/GNNSys21_paper_8.pdf) [[code]](https://github.com/zhiqi-0/PaGraph)
- **[arXiv 2019]** TigerGraph: A Native MPP Graph Database (*UCSD*) [[paper]](https://arxiv.org/pdf/1901.08248.pdf)

### GNN Training Accelerators

- **[ISCA 2022]** Hyperscale FPGA-as-a-service architecture for large-scale distributed graph neural network (*Alibaba*) [[paper]](https://dl.acm.org/doi/abs/10.1145/3470496.3527439)
- **[arXiv 2021]** GCNear: A Hybrid Architecture for Efficient GCN Training with Near-Memory Processing (*PKU*) [[paper]](https://arxiv.org/abs/2111.00680)
- **[DATE 2021]** ReGraphX: NoC-enabled 3D Heterogeneous ReRAM Architecture for Training Graph Neural Networks (*WSU*) [[paper]](https://arxiv.org/abs/2102.07959)
- **[TCAD 2021]** Rubik: A Hierarchical Architecture for Efficient Graph Learning (*Chinese Academy of Sciences*) [[paper]](https://arxiv.org/pdf/2009.12495.pdf)
- **[FPGA 2020]** GraphACT: Accelerating GCN Training on CPU-FPGA Heterogeneous Platforms (*USC*) [[paper]](https://dl.acm.org/doi/pdf/10.1145/3373087.3375312) [[code]](https://github.com/GraphSAINT/GraphACT)

### GNN Inference Accelerators

- **[IPDPS 2022]** Understanding the Design Space of Sparse/Dense Multiphase Dataflows for Mapping Graph Neural Networks on Spatial Accelerators (*GaTech*) [[paper]](https://arxiv.org/abs/2103.07977) [[code]](https://github.com/stonne-simulator/omega)
- **[HPCA 2022]** GCoD: Graph Convolutional Network Acceleration via Dedicated Algorithm and Accelerator Co-Design (*Rice, PNNL*) [[paper]](https://arxiv.org/abs/2112.11594) [[code]](https://github.com/RICE-EIC/GCoD)
- **[DAC 2021]** DyGNN: Algorithm and Architecture Support of vertex Dynamic Pruning for Graph Neural Networks (*Hunan University*) [[paper]](https://ieeexplore.ieee.org/document/9586298)
- **[DAC 2021]** BlockGNN: Towards Efficient GNN Acceleration Using Block-Circulant Weight Matrices (*PKU*) [[paepr]](https://arxiv.org/abs/2104.06214)
- **[DAC 2021]** TARe: Task-Adaptive in-situ ReRAM Computing for Graph Learning (*Chinese Academy of Sciences*) [[paper]](https://ieeexplore.ieee.org/abstract/document/9586193)
- **[ICCAD 2021]** G-CoS: GNN-Accelerator Co-Search Towards Both Better Accuracy and Efficiency (*Rice*) [[paper]](https://arxiv.org/abs/2109.08983)
- **[MICRO 2021]** I-GCN: A Graph Convolutional Network Accelerator with Runtime Locality Enhancement through Islandization (*PNNL*) [[paper]](https://dl.acm.org/doi/pdf/10.1145/3466752.3480113)
- **[arXiv 2021]** ZIPPER: Exploiting Tile- and Operator-level Parallelism for General and Scalable Graph Neural Network Acceleration (*SJTU*) [[paper]](https://arxiv.org/abs/2107.08709)
- **[TComp 2021]** EnGN: A High-Throughput and Energy-Efficient Accelerator for Large Graph Neural Networks (*Chinese Academy of Sciences*) [[paper]](https://arxiv.org/abs/1909.00155)
- **[HPCA 2021]** GCNAX: A Flexible and Energy-efficient Accelerator for Graph Convolutional Neural Networks (*GWU*) [[paper]](https://ieeexplore.ieee.org/abstract/document/9407104)
- **[APA 2020]** GNN-PIM: A Processing-in-Memory Architecture for Graph Neural Networks (*PKU*) [[paper]](http://115.27.240.201/docs/20200915165942122459.pdf)
- **[ASAP 2020]** Hardware Acceleration of Large Scale GCN Inference (*USC*) [[paper]](https://ieeexplore.ieee.org/document/9153263)
- **[DAC 2020]** Hardware Acceleration of Graph Neural Networks (*UIUC*) [[paper]](http://rakeshk.web.engr.illinois.edu/dac20.pdf)
- **[MICRO 2020]** AWB-GCN: A graph convolutional network accelerator with runtime workload rebalancing (*PNNL*) [[paper]](https://ieeexplore.ieee.org/abstract/document/9252000)
- **[arXiv 2020]** GRIP: A Graph Neural Network Accelerator Architecture (*Stanford*) [[paper]](https://arxiv.org/pdf/2007.13828.pdf)
- **[HPCA 2020]** HyGCN: A GCN Accelerator with Hybrid Architecture (*UCSB*) [[paper]](https://arxiv.org/pdf/2001.02514.pdf) 
