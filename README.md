# SyVOLT

This is the repository for the SyVOLT contract verification tool.

## Objective

We address the issue of model transformation verification with our technique for verifying visual pre-/post-condition contracts on DSLTrans model transformations. A contract is said to hold on a transformation if it holds on the transformation’s input- output pairs. That is, for all input models where the contract’s pre-condition holds, the contract’s post-condition also holds in the corresponding output model produced by executing the transformation. Traceability constraints between the elements of the input and output models may also be required. Otherwise, the contract does not hold, and consequently, the transformation does not correctly implement the contract.

For more information, including a demo of the prover: <a href="https://youtu.be/8PrR5RhPptY">SyVOLT Contract Prover Video</a><br>

## Installation

Please see the INSTALL.txt file in this directory.

The main development and usage platform is Linux. SyVOLT may not work on MacOS or Windows.

## Usage

### Command-line
- Run the test script using Python
  - Example: 'python test_atlTrans_extended.py'
- Use the argument `--help` to see some useful arguments
  * `--slice=N` will slice the transformation for contract N
  * `--contract=N` will select only one contract to prove, but will not slice
  * `--verbosity=2` will output many details of path condition construction
  * `--load` will attempt to load PCs generated previously, to begin contract proving immediately

### Eclipse
- Install the DSLTrans and SyVOLT plugins to edit and visualize the transformations and contracts
- Run the ANT script (such as verify_mbeddr.xml) to start the prover

### MPS
The MPS plugin can be downloaded at: https://plugins.jetbrains.com/plugin/10385-dsltrans
Please see the plugin repository for usage instructions: https://github.com/mbeddr/language_verification/blob/master/README.md

### Mutation Testing
For mutation testing, edit and run the `do_mutation_testing.py` file in the root directory.

This will use the file `mutation/mutation_possibilities.py` to generate all possible mutations on the transformation.

## Related Work
<a href="http://www.sable.mcgill.ca/~clump/theses/oakes-18-symbolic-TH.pdf">[6]</a> <i>A Symbolic Execution-Based Approach To Model Transformation Verification using Structural Contracts</i>. B. Oakes.  Ph.D. dissertation, McGill University, 2018. <br>

<a href="https://repository.uantwerpen.be/docman/irua/d4a3c4/155126.pdf">[6]</a> <i>Debugging of Model Transformations and Contracts in SyVOLT</i>. B. Oakes, L. Lúcio, C. Verbrugge, H. Vangheluwe. Proceedings of MDEbug co-located with MODELS 2018, 532-537. 2018.<br>

<a href="http://msdl.cs.mcgill.ca/people/bentley/research/paper_sosym_2016.pdf">[6]</a> <i>Full Contract Verification for ATL using Symbolic Execution</i>. B. Oakes, J. Troya, L. Lúcio, M. Wimmer. Software and Systems Modeling 2016 (pp. 1-35). Springer Berlin Heidelberg. <br>

<a href="http://msdl.cs.mcgill.ca/people/bentley/research/paper1.pdf">[5]</a> <i>SyVOLT: Full Model Transformation Verification Using Contracts</i>. L. Lúcio, B. Oakes, C. Gomes, G. Selim, J. Dingel, J. R. Cordy, H. Vangheluwe. Proceedings of MODELS 2015.<br>

<a href="http://msdl.cs.mcgill.ca/people/bentley/research/paper_PD_MoDELS_2015.pdf">[4]</a> <i>Finding and Fixing Bugs in Model Transformations with Formal Verification: An Experience Report</i>. G. Selim, J. R. Cordy, J. Dingel, L. Lúcio, B. Oakes. Proceedings of Analysis of Model Transformations 2015 (pp. 26-35).<br>

<a href="http://msdl.cs.mcgill.ca/people/bentley/research/paper_models_2015.pdf">[3]</a> <i>Fully Verifying Transformation Contracts for Declarative ATL</i>. B. Oakes, J. Troya, L. Lúcio, M. Wimmer. Proceedings of MODELS 2015 (pp. 256-265).<br>

<a href="http://msdl.cs.mcgill.ca/people/bentley/research/syvolttechreport">[2]</a> <i>A Technique for Symbolically Verifying Properties of Graph-based Model Transformations</i>. L. Lúcio, B. Oakes, H. Vangheluwe. Technical Report SOCS-TR-2014.1, McGill University.<br>

<a href="http://msdl.cs.mcgill.ca/people/bentley/research/SyVoltICGT">[1]</a> <i>Specification and Verification of Graph-Based Model Transformation Properties</i>. G. Selim, L. Lúcio, J. Cordy, J. Dingel, B.Oakes. Proceedings of <i>Graph Transformation</i> 2014 (pp. 113-129). Springer International Publishing.<br>
