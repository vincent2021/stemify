# A simple Vue + Python app based on Deezer spleeter tool
## Installation
Backend: conda should be installed first, then in the __back__ folder create the env with:
> conda env create -f 'env/gpu.yml'
or
> conda env create -f 'env/cpu.yml'
if you can't use tensorflow-gpu and CUDA driver (MacOS X for example)

Frontend: Node.js should be installed first, then in the __front_ folder run:
> npm install

## Starting the app
1. go to the __back__ folder and use "start.sh"
2. go to the __front__ folder and run "npm run serve"
