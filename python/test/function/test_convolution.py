# Copyright (c) 2017 Sony Corporation. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from __future__ import division

import pytest
import numpy as np
import nnabla as nn
import nnabla.functions as F
import refs
from nbla_test_utils import list_context

ctxs = list_context('Convolution')


def ref_convolution(x, w, b, base_axis, pad, stride, dilation, group):
    y = []
    for xx in x.reshape((-1,) + x.shape[base_axis:]):
        y += [refs.convolution_nd(xx, w, b, pad, stride,
                                  dilation, group)[np.newaxis]]
    y = np.vstack(y)
    return y.reshape(x.shape[:base_axis] + y.shape[1:])


def core_test_convolution_forward_backward(inshape, kernel, outmaps, pad, stride,
                                           dilation, group, with_bias, seed, ctx,
                                           func_name):
    from nbla_test_utils import function_tester
    rng = np.random.RandomState(seed)
    i = rng.randn(*inshape).astype(np.float32)
    inmaps = inshape[-len(kernel) - 1]
    kshape = (outmaps,) + (inmaps // group,) + kernel
    k = rng.randn(*kshape).astype(np.float32)
    base_axis = len(inshape) - len(kernel) - 1
    b = None
    if with_bias:
        b = rng.randn(outmaps).astype(np.float32)
    inputs = [i, k, b]
    function_tester(rng, F.convolution, ref_convolution, inputs,
                    func_args=[base_axis, pad, stride, dilation, group],
                    atol_f=1e-4, atol_b=1e-2, atol_accum=1e-5, dstep=1e-2,
                    ctx=ctx, func_name=func_name)


@pytest.mark.parametrize("ctx, func_name", ctxs)
@pytest.mark.parametrize("seed", [313])
@pytest.mark.parametrize("inshape, kernel, outmaps, pad, stride, dilation", [
    ((2, 2, 10), (1,), 4, (3,), (2,), (1,)),
    ((2, 2, 10), (3,), 2, (0,), (1,), (2,)),
])
@pytest.mark.parametrize("group", [1, 2])
@pytest.mark.parametrize("with_bias", [True, False])
def test_convolution_1d_forward_backward(inshape, kernel, outmaps, pad, stride,
                                         dilation, group, with_bias, seed, ctx,
                                         func_name):
    if func_name == 'ConvolutionCuda':
        pytest.skip('CUDA Convolution N-D is only supported in CUDNN extension')
    core_test_convolution_forward_backward(inshape, kernel, outmaps, pad, stride,
                                           dilation, group, with_bias, seed, ctx,
                                           func_name)


@pytest.mark.parametrize("ctx, func_name", ctxs)
@pytest.mark.parametrize("seed", [313])
@pytest.mark.parametrize("inshape, kernel, outmaps, pad, stride, dilation", [
    ((2, 2, 10, 10), (3, 2), 4, (3, 0), (1, 2), (2, 1)),
    ((2, 2, 10, 10), (3, 2), 4, (0, 0), (1, 1), (1, 1)),
])
@pytest.mark.parametrize("group", [1, 2])
@pytest.mark.parametrize("with_bias", [True, False])
def test_convolution_2d_forward_backward(inshape, kernel, outmaps, pad, stride,
                                         dilation, group, with_bias, seed, ctx,
                                         func_name):
    core_test_convolution_forward_backward(inshape, kernel, outmaps, pad, stride,
                                           dilation, group, with_bias, seed, ctx,
                                           func_name)


@pytest.mark.parametrize("ctx, func_name", ctxs)
@pytest.mark.parametrize("seed", [313])
@pytest.mark.parametrize("inshape, kernel, outmaps, pad, stride, dilation", [
    ((2, 2, 7, 8, 5), (2, 3, 2), 4, (3, 0, 0), (1, 2, 1), (2, 1, 1)),
])
@pytest.mark.parametrize("group", [1, 2])
@pytest.mark.parametrize("with_bias", [True, False])
def test_convolution_3d_forward_backward(inshape, kernel, outmaps, pad, stride,
                                         dilation, group, with_bias, seed, ctx,
                                         func_name):
    if func_name == 'ConvolutionCuda':
        pytest.skip('CUDA Convolution N-D is only supported in CUDNN extension')
    core_test_convolution_forward_backward(inshape, kernel, outmaps, pad, stride,
                                           dilation, group, with_bias, seed, ctx,
                                           func_name)
