const path = require('path');

module.exports = {
    entry: {app:'./src/app.ts',req:'./src/req.ts'}, 
    module: {
        rules: [
            {
                test: /\.ts$/,
                use: 'ts-loader',
                exclude: /node_modules/,
            }
        ]
    },
    output: {
        filename: '[name].js', 
        path: path.resolve(__dirname, './public'),
    },
};