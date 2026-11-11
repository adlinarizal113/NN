from activation_utils import tanh, show_app

show_app('Tanh', tanh, r'\tanh(x)=\frac{e^x-e^{-x}}{e^x+e^{-x}}',
         'Tanh maps every real input to a value between -1 and 1.')
