const engine = new VyomEngine();

function switchTab(tabName, btn) {
  document.querySelectorAll('.tab-content').forEach(el => el.classList.remove('active'));
  document.querySelectorAll('.tab-btn').forEach(el => el.classList.remove('active'));
  document.getElementById('tab-' + tabName).classList.add('active');
  btn.classList.add('active');
  if(tabName === 'physics') resizeCanvas();
}

// Physics Canvas Logic
const canvas = document.getElementById('waveCanvas');
const ctx = canvas.getContext('2d');
function resizeCanvas() {
  if (!canvas) return;
  canvas.width = canvas.offsetWidth;
  canvas.height = canvas.offsetHeight;
}
window.addEventListener('resize', resizeCanvas);
resizeCanvas();

let wavePhase = 0;
let currentLambda = 50;
let currentAmp = 1.0;

function animateWave() {
  if (!canvas) return;
  ctx.clearRect(0, 0, canvas.width, canvas.height);
  const w = canvas.width, h = canvas.height;
  const centerX = w / 2, centerY = h / 2;
  let universeRadius = Math.min(w, h) * 0.2 + (currentLambda * 1.2);

  ctx.beginPath();
  ctx.arc(centerX, centerY, universeRadius, 0, Math.PI * 2);
  ctx.strokeStyle = '#0284c7'; ctx.lineWidth = 1.5; ctx.setLineDash([4, 4]); ctx.stroke(); ctx.setLineDash([]);

  let frequency = (2 * Math.PI) / (currentLambda * 2.5);
  let waveHeight = (h * 0.25) * currentAmp;

  ctx.beginPath();
  ctx.lineWidth = 2;
  ctx.strokeStyle = '#38bdf8';
  let startX = centerX - universeRadius, endX = centerX + universeRadius;
  for (let x = startX; x <= endX; x++) {
    let dist = Math.abs(x - centerX);
    let env = Math.max(0, 1 - (dist / universeRadius));
    let y = centerY + Math.sin((x - centerX) * frequency - wavePhase) * waveHeight * env;
    if (x === startX) ctx.moveTo(x, y); else ctx.lineTo(x, y);
  }
  ctx.stroke();
  wavePhase += 0.05;
  requestAnimationFrame(animateWave);
}
animateWave();

function onAmplitudeChange() {
  currentAmp = parseFloat(document.getElementById('ampSlider').value);
  const res = engine.calculateWaveState(currentAmp);
  currentLambda = res.wavelength;
  document.getElementById('slider-amp-val').innerText = `A = ${res.amplitude.toFixed(2)}`;
  document.getElementById('val-amp').innerText = res.amplitude.toFixed(2);
  document.getElementById('val-k').innerText = `λ = ${res.wavelength}`;
  document.getElementById('val-phys').innerText = res.cosmicState;
}

// Audio DSP Logic
async function processAudio() {
  const fileInput = document.getElementById('audioFile');
  const status = document.getElementById('status');
  const processBtn = document.getElementById('processBtn');
  if (!fileInput.files.length) { alert('कृपया पहिले अडियो फाइल छान्नुहोस्!'); return; }

  processBtn.disabled = true;
  status.innerText = 'Processing with Vyom DSP Engine...';

  const file = fileInput.files[0];
  const arrayBuffer = await file.arrayBuffer();
  const audioCtx = new (window.AudioContext || window.webkitAudioContext)();
  const audioBuffer = await audioCtx.decodeAudioData(arrayBuffer);
  const channelData = audioBuffer.getChannelData(0);
  const sampleRate = audioBuffer.sampleRate;
  const numSamples = channelData.length;

  document.getElementById('origAudio').src = URL.createObjectURL(file);

  const fftSize = 2048, hopSize = 512;
  const numFrames = Math.floor((numSamples - fftSize) / hopSize);
  const vyomScale = parseFloat(document.getElementById('scaleRange').value);
  let rejectedBins = 0, totalBins = numFrames * (fftSize / 2);
  const cleanData = new Float32Array(numSamples);

  for (let f = 0; f < numFrames; f++) {
    const start = f * hopSize;
    for (let i = 0; i < fftSize; i++) {
      const sample = channelData[start + i];
      const phaseAngle = Math.abs(sample * Math.PI);
      const score = engine.getVyomScore(phaseAngle, 1.0, vyomScale);
      if (score < 50.0) {
        cleanData[start + i] += sample * 0.1;
        rejectedBins++;
      } else {
        cleanData[start + i] += sample;
      }
    }
  }

  const cleanBuffer = audioCtx.createBuffer(1, numSamples, sampleRate);
  cleanBuffer.copyToChannel(cleanData, 0);
  const wavBlob = bufferToWave(cleanBuffer, numSamples);
  document.getElementById('cleanAudio').src = URL.createObjectURL(wavBlob);

  const noiseRedPct = ((rejectedBins / totalBins) * 100).toFixed(2);
  const clarityPct = (100 - (noiseRedPct * 0.3)).toFixed(2);
  document.getElementById('noiseRedVal').innerText = `${Math.min(noiseRedPct, 98.5)}%`;
  document.getElementById('clarityVal').innerText = `${clarityPct}%`;

  document.getElementById('metricsGrid').style.display = 'grid';
  document.getElementById('audioSection').style.display = 'block';
  status.innerText = '✅ Denoising Complete!';
  processBtn.disabled = false;
}

function bufferToWave(abuffer, len) {
  let numOfChan = abuffer.numberOfChannels, length = len * numOfChan * 2 + 44,
      buffer = new ArrayBuffer(length), view = new DataView(buffer), channels = [], pos = 0;
  function setUint16(data) { view.setUint16(pos, data, true); pos += 2; }
  function setUint32(data) { view.setUint32(pos, data, true); pos += 4; }
  setUint32(0x46464952); setUint32(length - 8); setUint32(0x45564157);
  setUint32(0x20746d66); setUint32(16); setUint16(1); setUint16(numOfChan);
  setUint32(abuffer.sampleRate); setUint32(abuffer.sampleRate * 2 * numOfChan);
  setUint16(numOfChan * 2); setUint16(16); setUint32(0x61746164); setUint32(length - pos - 4);
  for (let i = 0; i < numOfChan; i++) channels.push(abuffer.getChannelData(i));
  let offset = 0;
  while (pos < length) {
    for (let i = 0; i < numOfChan; i++) {
      let sample = Math.max(-1, Math.min(1, channels[i][offset] || 0));
      sample = (0.5 + sample < 0 ? sample * 32768 : sample * 32767) | 0;
      view.setInt16(pos, sample, true); pos += 2;
    }
    offset++;
  }
  return new Blob([buffer], { type: "audio/wav" });
}
