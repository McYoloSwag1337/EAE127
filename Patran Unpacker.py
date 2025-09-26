
from pyNastran.op2.op2 import OP2

# Load the OP2 file
op2 = OP2()
op2.read_op2('path_to_your_file.op2')

# Extract the stiffness matrix
stiffness_matrix = op2.matrices['K']  # 'K' refers to the global stiffness matrix
print(stiffness_matrix)
