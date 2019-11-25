#Node And Conda should be installed
cd back
#Installing Conda env
echo('Install and activate Conda env')
conda create --name  stemify
conda source activate stemify
echo('Starting API')
python3 api.py
echo('Starting a Redis Server and a Worker')
redis-server
rq
#Installing and starting Node.js & Vue frontend
echo('Install and launch Node.js')
cd ../front
npm install
npm run serve