const express = require('express');
const bodyParser = require('body-parser');
const axios = require('axios');

const app = express();

app.use(bodyParser.raw({ type: 'audio/wav', limit: '50mb' }));

app.post('/transcribe', async (req, res) => {
    const audioData = req.body;
    
    try {
        const response = await axios.post('https://api.openai.com/v1/engines/whisper/transcribe', {
            audio_data: audioData.toString('base64')
        }, {
            headers: {
                'Authorization': `Bearer YOUR_OPENAI_API_KEY`,
                'Content-Type': 'application/json'
            }
        });

        const transcription = response.data.data;
        res.json(transcription);
    } catch (error) {
        console.error('Error transcribing audio:', error);
        res.status(500).send('Failed to transcribe audio.');
    }
});

const PORT = 3000;
app.listen(PORT, () => {
    console.log(`Server is running on http://localhost:${PORT}`);
});
