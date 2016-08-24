# SyVOLT

This is the repository for the SyVOLT contract prover.

## Objective

We address the issue of model transformation verification with our technique for verifying visual pre-/post-condition contracts on DSLTrans model transformations. A contract is said to hold on a transformation if it holds on the transformation’s input- output pairs. That is, for all input models where the contract’s pre-condition holds, the contract’s post-condition also holds in the corresponding output model produced by executing the transformation. Traceability constraints between the elements of the input and output models may also be required. Otherwise, the contract does not hold, and consequently, the transformation does not correctly implement the contract.

For more information, including a demo of the prover: <a href="https://youtu.be/8PrR5RhPptY">SyVOLT Contract Prover Video</a><br>

## Installation

Please see the INSTALL.txt file in this directory.

## Usage

### Command-line
- Run the test script using Python
-- Example: 'python test_atlTrans_extended.py'
- Use the flag '--help' to see some useful arguments

### Eclipse
- Install the DSLTrans and SyVOLT plugins to edit and visualize the transformations and contracts
- Run the ANT script (such as verify_mbeddr.xml) to start the prover

### MPS
To be completed

## Related Work
<a href="http://msdl.cs.mcgill.ca/people/bentley/research/paper_sosym_2016.pdf">[6]</a> <i>Full Contract Verification for ATL using Symbolic Execution</i>. <b>B. Oakes</b>, J. Troya, L. Lúcio, M. Wimmer. Software and Systems Modeling 2016 (pp. 1-35). Springer Berlin Heidelberg. <br>

<a href="http://msdl.cs.mcgill.ca/people/bentley/research/paper1.pdf">[5]</a> <i>SyVOLT: Full Model Transformation Verification Using Contracts</i>. L. Lúcio, <b>B. Oakes</b>, C. Gomes, G. Selim, J. Dingel, J. R. Cordy, H. Vangheluwe. Proceedings of MODELS 2015.<br>

<a href="http://msdl.cs.mcgill.ca/people/bentley/research/paper_PD_MoDELS_2015.pdf">[4]</a> <i>Finding and Fixing Bugs in Model Transformations with Formal Verification: An Experience Report</i>. G. Selim, J. R. Cordy, J. Dingel, L. Lúcio, <b>B. Oakes</b>. Proceedings of Analysis of Model Transformations 2015 (pp. 26-35).<br>

<a href="http://msdl.cs.mcgill.ca/people/bentley/research/paper_models_2015.pdf">[3]</a> <i>Fully Verifying Transformation Contracts for Declarative ATL</i>. <b>B. Oakes</b>, J. Troya, L. Lúcio, M. Wimmer. Proceedings of MODELS 2015 (pp. 256-265).<br>

<a href="http://msdl.cs.mcgill.ca/people/bentley/research/syvolttechreport">[2]</a> <i>A Technique for Symbolically Verifying Properties of Graph-based Model Transformations</i>. L. Lúcio, <b>B. Oakes</b>, H. Vangheluwe. Technical Report SOCS-TR-2014.1, McGill University.<br>

<a href="http://msdl.cs.mcgill.ca/people/bentley/research/SyVoltICGT">[1]</a> <i>Specification and Verification of Graph-Based Model Transformation Properties</i>. G. Selim, L. Lúcio, J. Cordy, J. Dingel, <b>B.Oakes</b>. Proceedings of <i>Graph Transformation</i> 2014 (pp. 113-129). Springer International Publishing.<br>
