const path = require('path');
const { spawn } = require('child_process');

exports.getAnswer = (question) => {
    return new Promise((resolve, reject) => {
        const pythonProcess = spawn('python', [path.join(__dirname, '../../ml/chatbot_model.py'), question]);

        let data = '';
        pythonProcess.stdout.on('data', (chunk) => {
            data += chunk.toString();
        });

        pythonProcess.stderr.on('data', (error) => {
            console.error(`Python Error: ${error.toString()}`);
            reject(error.toString());
        });

        pythonProcess.on('close', (code) => {
            if (code === 0) {
                resolve(data.trim());
            } else {
                reject(`Python process exited with code ${code}`);
            }
        });
    });
};
