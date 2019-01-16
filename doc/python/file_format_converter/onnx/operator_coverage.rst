Operator support status
=======================

Support status importing from ONNX
----------------------------------

This is a status list of [ONNX operators](https://github.com/onnx/onnx/blob/master/docs/Operators.md)
that indicates if each operator can be converted to NNP.

- OK The ONNX operator can map to a NNabla operator.
- Not test means the ONNX operator has not been verified. It might be one of the following cases:
    - The ONNX operator hasn't been checked if it can be converted to NNabla.
    - The ONNX operator has been checked if it can be converted to NNabla, but the implementation has not started.
    - The solution is not perfect/finished, for example, the operator can map to a combination of NNabla operators.
    - Hard to find a solution with existing NNabla operators.

Total 0/108

As the following table, Opset column means the maximal opset version are supported to convert to NNP.
In user's model, if there is any function opset version exceed the maximal opset(as the following table), the importer
might fail to convert NNP model due to this function.

======================================== =============== =============== =================================================
Operator                                 Opset           Status          Description
======================================== =============== =============== =================================================
Abs                                      1,6             Not test
Add                                      1,6             Not test        broadcast will be converted to a BroadcastTo
And                                      1               Not test        broadcast will be converted to a BroadcastTo
ArgMax                                                   Unimplemented   Operator does not exist in NNabla
ArgMin                                                   Unimplemented   Operator does not exist in NNabla
AveragePool                              1               Not test        autopad not supported. pads must have same
                                                                         value for begin and end.
BatchNormalization                       1,6             Not test        is_test=false not supported (only inference)
Cast                                                     Unimplemented   Operator does not exist in NNabla(No type
                                                                         information is exposed in NNP)
Ceil                                                     Unimplemented   Should map to Ceil
Clip                                     6               Not test        Converted to Identity, MaximumScalar,
                                                                         MinimumScalar, or both depending on the attribute
Concat                                   1,4             Not test
Constant                                 1,9             Not test        Converted to an input parameter
Conv                                     1               Not test        auto_pad not supported. pads must have same value
                                                                         for begin and end.
ConvTranspose                                            Unimplemented   Should map to Deconvolution?
DepthToSpace                                             Unimplemented   Operator does not exist in NNabla
Div                                      1,6             Not test        broadcast will be converted to a BroadcastTo
Dropout                                  1,6,7           Not test        mask output will be removed since NNabla does
                                                                         not produce mask output.
Elu                                      1,6             Not test
Equal                                    1               Not test        broadcast will be converted to a BroadcastTo.
                                                                         Input data type will all be converted to int64
                                                                         since NNP does not have type information
Exp                                      1,6             Not test
Flatten                                                  Unimplemented   Operator does not exist in NNabla
Floor                                                    Unimplemented   Should map to Floor
GRU                                                      Unimplemented   Operator does not exist in NNabla
Gather                                                   Unimplemented   Operator does not exist in NNabla
Gemm                                     1,6,7,9         Not test        alpha and beta is not supported.
                                                                         Input A and B must be two dimensional,
                                                                         and input C must be one dimensional.
                                                                         transA, transB will be converted to
                                                                         a separate transpose operator
GlobalAveragePool                        1               Not test
GlobalLpPool                                             Unimplemented   Operator does not exist in NNabla
GlobalMaxPool                                            Unimplemented   Operator does not exist in NNabla
Greater                                  1               Not test        broadcast will be converted to a BroadcastTo
HardSigmoid                                              Unimplemented   Should be able to map to
                                                                         MulScalar+AddScalar+MinimumScalar+ReLU
Hardmax                                                  Unimplemented   Operator does not exist in NNabla
Identity                                 1               Not test
InstanceNormalization                                    Unimplemented   Operator does not exist in NNabla
LRN                                      1               Not test        Converted to
                                                                         PowScalar+Tranpose+SumPooling+Transpose+MulScalar+AddScalar+PowScalar.
                                                                         Currently only odd size is allowed.
LSTM                                                     Unimplemented
LeakyRelu                                1,6             Not test
Less                                     1               Not test        broadcast will be converted to a BroadcastTo
Log                                      1,6             Not test
LogSoftmax                               1               Not test        Converted to Exp+Sum+Log+Sub2.
                                                                         Only works on input shape like N*C*1*1
LpNormalization                                          Unimplemented   Operator does not exist in NNabla
LpPool                                                   Unimplemented   Operator does not exist in NNabla
MatMul                                   1,9             Not test
Max                                      1,6,8           Not test        Only input of two tensors is currently supported
MaxPool                                  1,8             Not test        auto_pad is not supported.
                                                                         pads must have same value for begin and end.
MaxRoiPool                                               Unimplemented   Operator does not exist in NNabla
Mean                                     1,6,8           Not test        Operator does not exist in NNabla
Min                                      1,6,8           Not test        Only input of two tensors is currently supported
Mul                                                      Unimplemented   broadcast will be converted to a BroadcastTo
Neg                                      1,6             Not test        Converted to MulScalar
Not                                                      Unimplemented
Or                                       1,7             Not test        broadcast will be converted to a BroadcastTo
PRelu                                    1,6             Not test
Pad                                      1,2             Not test        For NNP to ONNX conversion, input buffer's
                                                                         dimension is assumed to be 4D if the shape cannot be determined.
Pow                                      1               Not test        broadcast will be converted to a BroadcastTo
RNN                                                      Unimplemented   Operator does not exist in NNabla
RandomNormal                                             Unimplemented   Should be able to map to Randn
RandomNormalLike                                         Unimplemented   Operator does not exist in NNabla
RandomUniform                                            Unimplemented   Should be able to map to Rand
RandomUniformLike                                        Unimplemented   Operator does not exist in NNabla
Reciprocal                               1,6             Not test        Converted to RDivScalar
ReduceL1                                                 Unimplemented   Operator does not exist in NNabla
ReduceL2                                                 Unimplemented   Operator does not exist in NNabla
ReduceLogSum                                             Unimplemented   Operator does not exist in NNabla
ReduceLogSumExp                                          Unimplemented   Operator does not exist in NNabla
ReduceMax                                1               Not test
ReduceMean                               1               Not test
ReduceMin                                1               Not test
ReduceProd                               1               Not test
ReduceSum                                1               Not test
ReduceSumSquare                                          Unimplemented   Operator does not exist in NNabla
Relu                                     1,6             Not test
Reshape                                  1,5             Not test        Not completedly supported.
Selu                                     1,6             Not test
Sigmoid                                  1,6             Not test
Size                                                     Unimplemented   Operator does not exist in NNabla
Slice                                                    Unimplemented   Operator does not exist in NNabla
Softmax                                  1               Not test        Only works on input shape like N*C*1*1
Softplus                                 1               Not test        Converted to Exp + AddScalar + Log
Softsign                                 1               Not test        Converted to Abs + AddScalar + Div2
SpaceToDepth                                             Unimplemented   Operator does not exist in NNabla
Split                                                    Unimplemented   Operator does not exist in NNabla
Sqrt                                                     Unimplemented   Operator does not exist in NNabla
Squeeze                                                  Unimplemented   Operator does not exist in NNabla
Sub                                      1,6             Not test        broadcast will be converted to a BroadcastTo
Sum                                      1,6,8           Not test        Supporting two inputs only
Tanh                                     1,6             Not test
Tile                                                     Unimplemented   Operator does not exist in NNabla
TopK                                                     Unimplemented   Operator does not exist in NNabla
Transpose                                1               Not test
Unsqueeze                                                Unimplemented   Operator does not exist in NNabla
Xor                                      1               Not test        broadcast will be converted to a BroadcastTo
experimental ATen                                        Unimplemented
experimental Affine                                      Unimplemented
experimental ConstantFill                                Unimplemented
experimental Crop                                        Unimplemented
experimental FC                                          Unimplemented
experimental GRUUnit                                     Unimplemented
experimental GivenTensorFill                             Unimplemented
experimental If                                          Unimplemented
experimental ImageScaler                                 Unimplemented
experimental Loop                                        Unimplemented
experimental LoopIndexTensor                             Unimplemented
experimental MeanVarianceNormalization                   Unimplemented
experimental ParametricSoftplus                          Unimplemented
experimental Scale                                       Unimplemented
experimental ScaledTanh                                  Unimplemented
experimental ThresholdedRelu                             Unimplemented
experimental Upsample                                    Unimplemented
======================================== =============== =============== =================================================

Support status exporting to ONNX
----------------------------------

The column of opset means current operator is mapped with which the opset specifications. For example,
Affine() is converted to 3 onnx functions, Reshape@5, Flatten@1, Gemm@6 and so on. Hence, the exporter
will generate the onnx model which require the executor at least support opset 6, when the model contains
Affine() function.

Total 0/136

Neural Network Layer
++++++++++++++++++++

Count 0/11

======================================== =============== =============== =================================================
Operator                                 Opset           Status          Description
======================================== =============== =============== =================================================
Affine                                   1,5,6           Not test        Implemented by Reshape,Flatten,Gemm
Convolution                              1               Not test        Implemented by Conv
DepthwiseConvolution                     1               Not test        Implemented by Conv
Deconvolution                            1,6             Not test        Implemented by ConvTranspose,Add
DepthwiseDeconvolution                                   Not test        Not implemented
MaxPooling                               1               Not test        Implemented by MaxPool
AveragePooling                           1               Not test        Implemented by AveragePool
GlobalAveragePooling                     1               Not test        Implemented by GlobalAveragePool
SumPooling                               1               Not test        Implemented by Mul
Unpooling                                                Not test        Not implemented
Embed                                                    Not test        Not implemented
======================================== =============== =============== =================================================

Neural Network Activation Functions
+++++++++++++++++++++++++++++++++++

Count 0/11

======================================== =============== =============== =================================================
Operator                                 Opset           Status          Description
======================================== =============== =============== =================================================
Sigmoid                                  6               Not test        Implemented by Sigmoid
Swish                                                    Not test        Not implemented
Tanh                                     6               Not test        Implemented by Tanh
ReLU                                     6               Not test        Implemented by Relu
LeakyReLU                                6               Not test        Implemented by LeakyRelu
Softmax                                  1               Not test        Implemented by Softmax
ELU                                      6               Not test        Implemented by ELU
SELU                                     6               Not test        Implemented by SELU
CReLU                                                    Not test        Not implemented
CELU                                                     Not test        Not implemented
PReLU                                    6               Not test        Implemented by PRelu
======================================== =============== =================================================

Normalization
+++++++++++++

Count 0/4

======================================== =============== =============== =================================================
Operator                                 Opset           Status          Description
======================================== =============== =============== =================================================
BatchNormalization                       6               Not test        Implemented by InstanceNormalization,BatchNormalization
MeanSubtraction                                          Not test        Not implemented
ClipGradByValue                                          Not test        Not implemented
ClipGradByNorm                                           Not test        Not implemented
======================================== =============== =============== =================================================

Reduction
+++++++++

Count 0/7

======================================== =============== =============== =================================================
Operator                                 Opset           Status          Description
======================================== =============== =============== =================================================
Sum                                      1               Not test        Implemented by ReduceSum
Mean                                     1               Not test        Implemented by ReduceMean
Max                                      1               Not test        Implemented by ReduceMax
Min                                      1               Not test        Implemented by ReduceMin
Prod                                     1               Not test        Implemented by ReduceProd
ReduceSum                                                Not test        Not implemented
ReduceMean                                               Not test        Not implemented
======================================== =============== =============== =================================================

Arithmetic
++++++++++

Count 0/12

======================================== =============== =============== =================================================
Operator                                 Opset           Status          Description
======================================== =============== =============== =================================================
Add2                                     6               Not test        Implemented by Add
BcAdd2                                                   Not test        Not implemented
Sub2                                     1               Not test        Implemented by Sub
Mul2                                     1               Not test        Implemented by Mul
Div2                                     6               Not test        Implemented by Div
Pow2                                     1               Not test        Implemented by Pow
AddScalar                                6               Not test        Implemented by Add
MulScalar                                1               Not test        Implemented by Mul
PowScalar                                1               Not test        Implemented by Pow
RSubScalar                               6               Not test        Implemented by Sub
RDivScalar                               6               Not test        Implemented by Div
RPowScalar                               1               Not test        Implemented by Pow
======================================== =============== =============== =================================================

Logical
+++++++

Count 0/24

======================================== =============== =============== =================================================
Operator                                 Opset           Status          Description
======================================== =============== =============== =================================================
Sign                                                     Not test        Not implemented
Minimum2                                 6               Not test        Implemented by Min
Maximum2                                 6               Not test        Implemented by Max
MinimumScalar                            6               Not test        Implemented by Clip
MaximumScalar                            6               Not test        Implemented by Clip
LogicalAnd                               1               Not test        Implemented by And
LogicalOr                                1               Not test        Implemented by Or
LogicalXor                               1               Not test        Implemented by Xor
Equal                                    1               Not test        Implemented by Equal
NotEqual                                                 Not test        Not implemented
GreaterEqual                                             Not test        Not implemented
Greater                                  1               Not test        Implemented by Greater
LessEqual                                                Not test        Not implemented
Less                                     1               Not test        Implemented by Less
LogicalAndScalar                                         Not test        Not implemented
LogicalOrScalar                                          Not test        Not implemented
LogicalXorScalar                                         Not test        Not implemented
EqualScalar                                              Not test        Not implemented
NotEqualScalar                                           Not test        Not implemented
GreaterEqualScalar                                       Not test        Not implemented
GreaterScalar                                            Not test        Not implemented
LessEqualScalar                                          Not test        Not implemented
LessScalar                                               Not test        Not implemented
LogicalNot                               1               Not test        Implemented by Not
======================================== =============== =============== =================================================

Math
++++

Count 0/18

======================================== =============== =============== =================================================
Operator                                 Opset           Status          Description
======================================== =============== =============== =================================================
Constant                                                 Not test        Not implemented
Abs                                      6               Not test        Implemented by Abs
Exp                                      6               Not test        Implemented by Exp
Log                                      6               Not test        Implemented by Log
Identity                                 1               Not test        Implemented by Identity
BatchMatmul                              1               Not test        Implemented by Matmul
Round                                                    Not test        Not implemented
Sin                                                      Not test        Not implemented
Cos                                                      Not test        Not implemented
Tan                                                      Not test        Not implemented
Sinh                                                     Not test        Not implemented
Cosh                                                     Not test        Not implemented
ASin                                                     Not test        Not implemented
ACos                                                     Not test        Not implemented
ATan                                                     Not test        Not implemented
ASinh                                                    Not test        Not implemented
ACosh                                                    Not test        Not implemented
ATanh                                                    Not test        Not implemented
======================================== =============== =============== =================================================

Array Manipulation
++++++++++++++++++

Count 0/13

======================================== =============== =============== =================================================
Operator                                 Opset           Status          Description
======================================== =============== =============== =================================================
Concatenate                              4               Not test        Implemented by Concat
Split                                    1,2             Not test        Implemented by Split,Squeeze
Stack                                    1,4             Not test        Implemented by Unsqueeze,Concat
Slice                                    1               Not test        Implemented by Slice
Pad                                      2               Not test        Implemented by Pad
Transpose                                1               Not test        Implemented by Transpose
Broadcast                                                Not test        Not implemented
OneHot                                   1,5             Not test        Implemented by Flatten,Gather,Reshape
Flip                                     1               Not test        Implemented by Gather,Transpose,Identity
Shift                                                    Not test        Not implemented
Reshape                                  5               Not test        Implemented by Reshape
MatrixDiag                                               Not test        Not implemented
MatrixDiagPart                                           Not test        Not implemented
======================================== =============== =============== =================================================

Stochasticity
+++++++++++++

Count 0/10

======================================== =============== =============== =================================================
Operator                                 Opset           Status          Description
======================================== =============== =============== =================================================
Dropout                                  6               Not test        Implemented by Dropout
TopKData                                                 Not test        Not implemented
TopKGrad                                                 Not test        Not implemented
Rand                                                     Not test        Not implemented
Randint                                                  Not test        Not implemented
Randn                                                    Not test        Not implemented
RandomCrop                                               Not test        Not implemented
RandomFlip                                               Not test        Not implemented
RandomShift                                              Not test        Not implemented
ImageAugmentation                                        Not test        Not implemented
======================================== =============== =============== =================================================

Loss Functions
++++++++++++++

Count 0/9

======================================== =============== =============== =================================================
Operator                                 Opset           Status          Description
======================================== =============== =============== =================================================
SigmoidCrossEntropy                                      Not test        Not implemented
BinaryCrossEntropy                                       Not test        Not implemented
SoftmaxCrossEntropy                                      Not test        Not implemented
CategoricalCrossEntropy                                  Not test        Not implemented
SquaredError                                             Not test        Not implemented
AbsoluteError                                            Not test        Not implemented
HuberLoss                                                Not test        Not implemented
EpsilonInsensitiveLoss                                   Not test        Not implemented
KLMultinomial                                            Not test        Not implemented
======================================== =============== =============== =================================================

Quantization Neural Network Layers
++++++++++++++++++++++++++++++++++

Count 0/10

======================================== =============== =============== =================================================
Operator                                 Opset           Status          Description
======================================== =============== =============== =================================================
BinarySigmoid                            6               Not test        Implemented by HardSigmoid
BinaryTanh                                               Not test        Not implemented
BinaryConnectAffine                                      Not test        Not implemented
BinaryConnectConvolution                 1,5             Not test        Implemented by Conv,Reshape
BinaryWeightAffine                                       Not test        Not implemented
BinaryWeightConvolution                                  Not test        Not implemented
INQAffine                                                Not test        Not implemented
INQConvolution                                           Not test        Not implemented
FixedPointQuantize                                       Not test        Not implemented
Pow2Quantize                                             Not test        Not implemented
======================================== =============== =============== =================================================

Validation
++++++++++

Count 0/3

======================================== =============== =============== =================================================
Operator                                 Opset           Status          Description
======================================== =============== =============== =================================================
TopNError                                                Not test        Not implemented
BinaryError                                              Not test        Not implemented
ConfusionMatrix                                          Not test        Not implemented
======================================== =============== =============== =================================================

Unsupported,SpecialUse
++++++++++++++++++++++

Count 0/4

======================================== =============== =============== =================================================
Operator                                 Opset           Status          Description
======================================== =============== =============== =================================================
VATNoise                                                 Not test        Not implemented
Unlink                                                   Not test        Not implemented
Sink                                                     Not test        Not implemented
NmsDetection2d                                           Not test        Not implemented
======================================== =============== =============== =================================================
