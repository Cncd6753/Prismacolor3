<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Prismacolor Master - 36 Set Edition</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css" rel="stylesheet">
    <script src="https://cdn.jsdelivr.net/npm/marked/marked.min.js"></script>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&display=swap');
        
        body {
            font-family: 'Inter', sans-serif;
            background-color: #020617; /* Slate 950 */
            color: #e2e8f0;
            overflow: hidden;
            height: 100vh;
            width: 100vw;
        }

        .glass-panel {
            background: rgba(15, 23, 42, 0.95);
            backdrop-filter: blur(12px);
            border: 1px solid rgba(255, 255, 255, 0.1);
        }

        /* Interactive Elements */
        .pencil-card {
            transition: all 0.2s ease;
        }
        .pencil-card:hover {
            transform: translateX(4px);
            filter: brightness(1.1);
        }

        .canvas-wrapper {
            box-shadow: 0 20px 50px -10px rgba(0, 0, 0, 0.7);
            cursor: crosshair;
            display: flex;
            align-items: center;
            justify-content: center;
            width: 100%;
            height: 100%;
            overflow: hidden;
            background-image: 
                linear-gradient(45deg, #1e293b 25%, transparent 25%), 
                linear-gradient(-45deg, #1e293b 25%, transparent 25%), 
                linear-gradient(45deg, transparent 75%, #1e293b 75%), 
                linear-gradient(-45deg, transparent 75%, #1e293b 75%);
            background-size: 20px 20px;
            background-position: 0 0, 0 10px, 10px -10px, -10px 0px;
        }

        #mainCanvas {
            max-width: 100%;
            max-height: 100%;
            object-fit: contain; 
            width: auto;
            height: auto;
        }

        /* Custom Inputs */
        input[type="color"] {
            -webkit-appearance: none;
            border: none;
            width: 32px;
            height: 32px;
            border-radius: 50%;
            overflow: hidden;
            cursor: pointer;
        }
        input[type="color"]::-webkit-color-swatch-wrapper { padding: 0; }
        input[type="color"]::-webkit-color-swatch { border: 2px solid #475569; border-radius: 50%; }

        /* Custom Radio Buttons */
        .radio-label {
            cursor: pointer;
            display: flex;
            align-items: center;
            gap: 0.5rem;
            font-size: 0.75rem;
            color: #94a3b8;
            transition: color 0.2s;
        }
        .radio-label:hover { color: #e2e8f0; }
        .radio-input {
            appearance: none;
            background-color: #1e293b;
            margin: 0;
            font: inherit;
            color: currentColor;
            width: 1.15em;
            height: 1.15em;
            border: 1px solid #475569;
            border-radius: 50%;
            display: grid;
            place-content: center;
        }
        .radio-input::before {
            content: "";
            width: 0.65em;
            height: 0.65em;
            border-radius: 50%;
            transform: scale(0);
            transition: 120ms transform ease-in-out;
            box-shadow: inset 1em 1em #818cf8;
        }
        .radio-input:checked::before { transform: scale(1); }
        .radio-input:checked + span { color: #818cf8; font-weight: 600; }

        ::-webkit-scrollbar { width: 6px; height: 6px; }
        ::-webkit-scrollbar-track { background: #0f172a; }
        ::-webkit-scrollbar-thumb { background: #334155; border-radius: 3px; }
        ::-webkit-scrollbar-thumb:hover { background: #475569; }

        .recipe-card { animation: slideIn 0.3s cubic-bezier(0.16, 1, 0.3, 1); }
        @keyframes slideIn {
            from { opacity: 0; transform: translateY(20px) scale(0.95); }
            to { opacity: 1; transform: translateY(0) scale(1); }
        }

        .prose h3 { color: #818cf8; font-weight: bold; margin-top: 1em; margin-bottom: 0.5em; }
        .prose ul { list-style-type: disc; padding-left: 1.5em; color: #cbd5e1; }
        .prose li { margin-bottom: 0.5em; }
        .prose strong { color: #e2e8f0; }
        .prose p { margin-bottom: 0.8em; line-height: 1.6; color: #94a3b8; }
    </style>
</head>
<body class="flex flex-col h-screen w-screen overflow-hidden">

    <!-- Header -->
    <header class="h-14 bg-slate-900 border-b border-slate-700/50 flex items-center justify-between px-6 flex-shrink-0 z-20">
        <div class="flex items-center gap-3">
            <i class="fas fa-layer-group text-indigo-500 text-xl"></i>
            <h1 class="text-lg font-bold tracking-wide text-slate-100">Prisma<span class="text-indigo-400">Board</span> 36 Set</h1>
        </div>
        <div class="flex items-center gap-4">
            <span id="fileNameDisplay" class="text-xs font-mono text-slate-400 hidden md:block"></span>
            <button id="resetBtn" class="bg-slate-800 hover:bg-slate-700 text-white px-3 py-1.5 rounded text-xs font-medium transition hidden border border-slate-600">
                New Project
            </button>
        </div>
    </header>

    <!-- Main Layout -->
    <main class="flex-1 flex flex-col lg:flex-row overflow-hidden relative h-full">
        
        <!-- CANVAS AREA (Left) -->
        <section class="flex-1 bg-slate-950 relative flex flex-col items-center justify-center p-4 overflow-hidden h-full" id="dropZone">
            
            <!-- Upload UI -->
            <div id="uploadPrompt" class="text-center p-16 border-2 border-dashed border-slate-700/50 rounded-2xl hover:border-indigo-500/50 hover:bg-slate-900/30 transition cursor-pointer group">
                <div class="w-20 h-20 bg-slate-900 rounded-full flex items-center justify-center mx-auto mb-6 group-hover:scale-110 transition duration-300 shadow-xl shadow-black/50">
                    <i class="fas fa-image text-3xl text-indigo-400"></i>
                </div>
                <h2 class="text-2xl font-semibold mb-2 text-slate-200">Drop Reference Image</h2>
                <p class="text-slate-500 mb-6 text-sm">Strictly matched to the 36-count box.</p>
                <button class="bg-indigo-600 hover:bg-indigo-500 text-white px-8 py-3 rounded-full font-medium shadow-lg shadow-indigo-900/20 transition hover:shadow-indigo-600/30">
                    Select File
                </button>
                <input type="file" id="fileInput" accept="image/*" class="hidden">
            </div>

            <!-- Canvas Wrapper -->
            <div id="canvasContainer" class="hidden canvas-wrapper rounded-lg border border-slate-800 bg-slate-900 w-full h-full relative">
                <canvas id="mainCanvas"></canvas>
                
                <!-- Hover Tooltip -->
                <div id="hoverTooltip" class="fixed pointer-events-none bg-black/80 border border-white/10 text-white text-xs rounded-md px-2 py-1 hidden z-50 backdrop-blur-sm whitespace-nowrap">
                    <span id="hoverCoords"></span>
                </div>

                <!-- Color Recipe Popup -->
                <div id="recipePopup" class="absolute bottom-4 right-4 w-72 glass-panel rounded-xl p-4 hidden recipe-card shadow-2xl z-40 border-l-4 border-indigo-500">
                    <div class="flex justify-between items-start mb-3">
                        <h3 class="text-sm font-bold text-white uppercase tracking-wider"><i class="fas fa-flask mr-2"></i>36-Set Recipe</h3>
                        <button id="closeRecipe" class="text-slate-500 hover:text-white"><i class="fas fa-times"></i></button>
                    </div>
                    
                    <div class="flex items-center gap-3 mb-4">
                        <div id="targetColorPreview" class="w-12 h-12 rounded-full border-2 border-white/20 shadow-inner"></div>
                        <div class="text-xs text-slate-300">
                            <p>Target Pixel</p>
                            <p class="font-mono text-[10px] opacity-50" id="targetRgbText">RGB(0,0,0)</p>
                        </div>
                    </div>

                    <div class="space-y-3" id="recipeSteps">
                        <!-- Dynamic Content injected here -->
                    </div>
                </div>
            </div>
            
            <div id="instructionText" class="absolute bottom-6 text-slate-500 text-xs hidden animate-pulse pointer-events-none bg-slate-900/50 px-3 py-1 rounded">
                <i class="fas fa-mouse-pointer mr-2"></i>Click image to see layering recipe
            </div>

        </section>

        <!-- SIDEBAR (Right) -->
        <aside class="w-full lg:w-[420px] bg-slate-900 border-l border-slate-800 flex flex-col z-10 shadow-2xl h-full overflow-hidden">
            
            <div class="flex-shrink-0">
                <!-- Paper Settings -->
                <div class="p-5 border-b border-slate-800 bg-slate-900">
                    <h2 class="text-xs font-bold uppercase tracking-widest text-indigo-400 mb-3 flex items-center gap-2">
                        <i class="fas fa-scroll"></i> Paper / Surface
                    </h2>
                    
                    <div class="grid grid-cols-[1fr_auto] gap-3 mb-3">
                        <select id="paperTypeSelect" class="bg-slate-800 border border-slate-700 text-white text-sm rounded-lg focus:ring-indigo-500 focus:border-indigo-500 block w-full p-2.5">
                            <option value="white" data-color="#FFFFFF">Standard White</option>
                            <option value="tonedTan" data-color="#B89B7D">Strathmore Toned Tan</option>
                            <option value="tonedGray" data-color="#9C9C9C">Strathmore Toned Gray</option>
                            <option value="black" data-color="#1A1A1A">Black Cardstock</option>
                            <option value="cream" data-color="#FFFDD0">Cream / Bristol Smooth</option>
                            <option value="kraft" data-color="#C2A278">Kraft Paper</option>
                            <option value="blueGrey" data-color="#475569">Dark Blue Grey</option>
                            <option value="custom">Custom Color...</option>
                        </select>
                        <input type="color" id="customPaperPicker" value="#ffffff" title="Custom Paper Color" disabled class="opacity-50">
                    </div>
                    <div id="paperPreview" class="h-6 w-full rounded border border-slate-700 mb-2 flex items-center justify-center text-[10px] text-slate-500/50 uppercase font-bold tracking-widest" style="background-color: #ffffff;">
                        Active Surface
                    </div>
                </div>

                <!-- Display Settings -->
                <div class="px-5 py-4 border-b border-slate-800 bg-slate-900/50">
                    <div class="flex justify-between items-center mb-3">
                        <h2 class="text-xs font-bold uppercase tracking-widest text-slate-400">Color Values</h2>
                    </div>
                    <div class="flex gap-4">
                        <label class="radio-label">
                            <input type="radio" name="displayMode" value="id" checked class="radio-input">
                            <span>Pencil ID</span>
                        </label>
                        <label class="radio-label">
                            <input type="radio" name="displayMode" value="rgb" class="radio-input">
                            <span>RGB</span>
                        </label>
                        <label class="radio-label">
                            <input type="radio" name="displayMode" value="cmyk" class="radio-input">
                            <span>CMYK</span>
                        </label>
                    </div>
                </div>

                <!-- Palette Count -->
                <div class="px-5 py-4 border-b border-slate-800 bg-slate-900">
                    <div class="flex justify-between items-center mb-2">
                        <h2 class="text-xs font-bold uppercase tracking-widest text-slate-400">Palette Size</h2>
                        <span id="countDisplay" class="text-xs font-mono text-indigo-300">24 Pencils</span>
                    </div>
                    <input type="range" id="colorCountInput" min="8" max="36" value="24" step="4" class="w-full h-1.5 bg-slate-700 rounded-lg appearance-none cursor-pointer accent-indigo-500">
                </div>
            </div>

            <!-- List Area -->
            <div id="pencilList" class="flex-1 overflow-y-auto p-4 space-y-2 relative bg-slate-950 min-h-0">
                <!-- Empty State -->
                <div class="absolute inset-0 flex flex-col items-center justify-center text-slate-600 pointer-events-none" id="emptyState">
                    <i class="fas fa-pencil-alt text-2xl mb-3 opacity-30"></i>
                    <p class="text-xs uppercase tracking-wide">Ready for Image</p>
                </div>
            </div>

            <!-- AI & Download Buttons -->
            <div class="flex-shrink-0 bg-slate-800 border-t border-slate-800">
                <div class="p-3">
                    <button id="aiGuideBtn" class="w-full bg-gradient-to-r from-indigo-600 to-violet-600 hover:from-indigo-500 hover:to-violet-500 text-white py-2 rounded-lg text-xs font-bold shadow-lg transition flex items-center justify-center gap-2 disabled:opacity-50 disabled:cursor-not-allowed group" disabled>
                        <i class="fas fa-magic group-hover:animate-pulse"></i> Generate Art Guide (36 Set) ✨
                    </button>
                </div>
                <div class="grid grid-cols-2 gap-px bg-slate-900">
                    <button id="downloadBtn" class="bg-slate-800 hover:bg-slate-700 text-slate-300 py-3 text-xs font-semibold transition flex items-center justify-center gap-2 disabled:opacity-50" disabled>
                        <i class="fas fa-file-download"></i> Save List
                    </button>
                    <button id="copyListBtn" class="bg-slate-800 hover:bg-slate-700 text-indigo-300 py-3 text-xs font-semibold transition flex items-center justify-center gap-2 disabled:opacity-50" disabled>
                        <i class="far fa-copy"></i> Copy
                    </button>
                </div>
            </div>

        </aside>

        <!-- AI Modal -->
        <div id="aiModal" class="fixed inset-0 z-50 bg-black/80 backdrop-blur-sm hidden flex items-center justify-center p-4">
            <div class="bg-slate-900 border border-slate-700 w-full max-w-2xl max-h-[80vh] rounded-xl flex flex-col shadow-2xl relative">
                <div class="p-4 border-b border-slate-700 flex justify-between items-center bg-slate-800/50 rounded-t-xl">
                    <h2 class="text-lg font-bold text-white flex items-center gap-2">
                        <i class="fas fa-robot text-indigo-400"></i> AI Art Coach ✨
                    </h2>
                    <button id="closeAiModal" class="text-slate-400 hover:text-white transition">
                        <i class="fas fa-times text-xl"></i>
                    </button>
                </div>
                <div class="flex-1 overflow-y-auto p-6 bg-slate-900/90 custom-scrollbar">
                    <div id="aiLoading" class="hidden flex flex-col items-center justify-center py-12">
                        <div class="w-10 h-10 border-4 border-indigo-500 border-t-transparent rounded-full animate-spin mb-4"></div>
                        <p class="text-indigo-300 font-medium animate-pulse">Analyzing textures & light...</p>
                    </div>
                    <div id="aiContent" class="prose prose-invert prose-sm max-w-none hidden"></div>
                </div>
                <div class="p-3 border-t border-slate-800 bg-slate-950 text-[10px] text-slate-500 text-center rounded-b-xl">
                    Generated by Gemini 2.5 Flash • Limited to Prismacolor 36 Set.
                </div>
            </div>
        </div>

    </main>

    <script>
        // --- API KEY CONFIGURATION ---
        const apiKey = ""; // Provided by environment

        // --- PRISMACOLOR 36 SET DATABASE ---
        // Strictly matched to Official Premier Soft Core 36-Count Box (Item 3598T)
        // Metallics removed. White retained.
        const prismacolorDB = [
            { id: 'PC914', name: 'Cream', rgb: [246, 237, 203] },
            { id: 'PC916', name: 'Canary Yellow', rgb: [253, 219, 29] },
            { id: 'PC1002', name: 'Yellowed Orange', rgb: [242, 152, 39] },
            { id: 'PC1003', name: 'Spanish Orange', rgb: [235, 137, 55] },
            { id: 'PC1034', name: 'Goldenrod', rgb: [218, 156, 42] },
            { id: 'PC918', name: 'Orange', rgb: [238, 114, 38] },
            { id: 'PC921', name: 'Pale Vermilion', rgb: [234, 88, 52] },
            { id: 'PC922', name: 'Poppy Red', rgb: [224, 53, 44] },
            { id: 'PC926', name: 'Carmine Red', rgb: [168, 30, 56] },
            { id: 'PC924', name: 'Crimson Red', rgb: [175, 29, 45] },
            { id: 'PC994', name: 'Process Red', rgb: [219, 44, 82] },
            { id: 'PC995', name: 'Mulberry', rgb: [136, 47, 85] },
            { id: 'PC929', name: 'Pink', rgb: [232, 127, 149] },
            { id: 'PC927', name: 'Light Peach', rgb: [243, 204, 181] },
            { id: 'PC939', name: 'Peach', rgb: [239, 181, 148] },
            { id: 'PC1008', name: 'Parma Violet', rgb: [109, 83, 137] },
            { id: 'PC932', name: 'Violet', rgb: [66, 44, 102] },
            { id: 'PC933', name: 'Violet Blue', rgb: [37, 45, 99] },
            { id: 'PC902', name: 'Ultramarine', rgb: [37, 54, 104] },
            { id: 'PC903', name: 'True Blue', rgb: [26, 60, 109] },
            { id: 'PC904', name: 'Light Cerulean Blue', rgb: [89, 149, 189] },
            { id: 'PC901', name: 'Indigo Blue', rgb: [23, 49, 75] },
            { id: 'PC992', name: 'Light Aqua', rgb: [140, 203, 191] },
            { id: 'PC989', name: 'Chartreuse', rgb: [187, 199, 47] },
            { id: 'PC912', name: 'Apple Green', rgb: [126, 167, 59] },
            { id: 'PC910', name: 'True Green', rgb: [29, 115, 59] },
            { id: 'PC909', name: 'Grass Green', rgb: [65, 105, 50] },
            { id: 'PC911', name: 'Olive Green', rgb: [73, 88, 43] },
            { id: 'PC908', name: 'Dark Green', rgb: [27, 65, 46] },
            { id: 'PC941', name: 'Light Umber', rgb: [129, 100, 77] },
            { id: 'PC943', name: 'Burnt Ochre', rgb: [162, 107, 48] },
            { id: 'PC945', name: 'Sienna Brown', rgb: [125, 62, 38] },
            { id: 'PC937', name: 'Tuscan Red', rgb: [115, 47, 51] },
            { id: 'PC946', name: 'Dark Brown', rgb: [78, 51, 38] },
            { id: 'PC935', name: 'Black', rgb: [25, 25, 25] },
            { id: 'PC938', name: 'White', rgb: [248, 248, 248] }
        ];

        // --- GLOBAL STATE ---
        const els = {
            dropZone: document.getElementById('dropZone'),
            uploadPrompt: document.getElementById('uploadPrompt'),
            canvasContainer: document.getElementById('canvasContainer'),
            canvas: document.getElementById('mainCanvas'),
            fileInput: document.getElementById('fileInput'),
            pencilList: document.getElementById('pencilList'),
            emptyState: document.getElementById('emptyState'),
            resetBtn: document.getElementById('resetBtn'),
            countInput: document.getElementById('colorCountInput'),
            countDisplay: document.getElementById('countDisplay'),
            copyBtn: document.getElementById('copyListBtn'),
            downloadBtn: document.getElementById('downloadBtn'),
            fileNameDisplay: document.getElementById('fileNameDisplay'),
            instructionText: document.getElementById('instructionText'),
            hoverTooltip: document.getElementById('hoverTooltip'),
            hoverCoords: document.getElementById('hoverCoords'),
            recipePopup: document.getElementById('recipePopup'),
            closeRecipe: document.getElementById('closeRecipe'),
            targetColorPreview: document.getElementById('targetColorPreview'),
            targetRgbText: document.getElementById('targetRgbText'),
            recipeSteps: document.getElementById('recipeSteps'),
            paperTypeSelect: document.getElementById('paperTypeSelect'),
            customPaperPicker: document.getElementById('customPaperPicker'),
            paperPreview: document.getElementById('paperPreview'),
            aiGuideBtn: document.getElementById('aiGuideBtn'),
            aiModal: document.getElementById('aiModal'),
            closeAiModal: document.getElementById('closeAiModal'),
            aiContent: document.getElementById('aiContent'),
            aiLoading: document.getElementById('aiLoading'),
            displayModeInputs: document.querySelectorAll('input[name="displayMode"]')
        };

        let currentImage = null;
        let currentFileName = "palette";
        let ctx = els.canvas.getContext('2d', { willReadFrequently: true });
        let activePencilSet = []; 
        let currentPaperRGB = [255, 255, 255];
        let currentPaperName = "Standard White";
        let currentDisplayMode = 'id';

        // --- MATH HELPERS ---
        function hexToRgb(hex) {
            var result = /^#?([a-f\d]{2})([a-f\d]{2})([a-f\d]{2})$/i.exec(hex);
            return result ? [
                parseInt(result[1], 16),
                parseInt(result[2], 16),
                parseInt(result[3], 16)
            ] : [255, 255, 255];
        }

        function rgbToCmyk(r, g, b) {
            let c = 1 - (r / 255);
            let m = 1 - (g / 255);
            let y = 1 - (b / 255);
            let k = Math.min(c, Math.min(m, y));

            c = (c - k) / (1 - k);
            m = (m - k) / (1 - k);
            y = (y - k) / (1 - k);

            if (k === 1) return { c:0, m:0, y:0, k:100 };
            if (isNaN(c)) c = 0; 

            return {
                c: Math.round(c * 100),
                m: Math.round(m * 100),
                y: Math.round(y * 100),
                k: Math.round(k * 100)
            };
        }

        function getPencilValue(pencil) {
            if (currentDisplayMode === 'rgb') {
                return `RGB(${pencil.rgb.join(', ')})`;
            } else if (currentDisplayMode === 'cmyk') {
                const cmyk = rgbToCmyk(pencil.rgb[0], pencil.rgb[1], pencil.rgb[2]);
                return `C${cmyk.c} M${cmyk.m} Y${cmyk.y} K${cmyk.k}`;
            }
            return pencil.id; 
        }

        function getColorDistance(rgb1, rgb2) {
            let rmean = (rgb1[0] + rgb2[0]) / 2;
            let r = rgb1[0] - rgb2[0];
            let g = rgb1[1] - rgb2[1];
            let b = rgb1[2] - rgb2[2];
            return Math.sqrt((((512 + rmean) * r * r) >> 8) + 4 * g * g + (((767 - rmean) * b * b) >> 8));
        }

        // --- CORE LOGIC ---

        function findClosestPencil(rgb) {
            let minDist = Infinity;
            let closest = prismacolorDB[0];
            for (let pencil of prismacolorDB) {
                let dist = getColorDistance(rgb, pencil.rgb);
                if (dist < minDist) {
                    minDist = dist;
                    closest = pencil;
                }
            }
            return { pencil: closest, dist: minDist };
        }

        function extractPalette(imgData, k) {
            const pixels = [];
            for (let i = 0; i < imgData.data.length; i += 100) {
                if (imgData.data[i+3] > 128) { 
                    pixels.push([imgData.data[i], imgData.data[i+1], imgData.data[i+2]]);
                }
            }
            if (pixels.length === 0) return [];
            let centroids = [];
            for (let i = 0; i < k; i++) centroids.push(pixels[Math.floor(Math.random() * pixels.length)]);

            for (let iter = 0; iter < 10; iter++) {
                const assignments = new Array(k).fill(0).map(() => ({ r: 0, g: 0, b: 0, count: 0 }));
                for (let p of pixels) {
                    let closestIdx = 0;
                    let closestDist = Infinity;
                    for (let c = 0; c < k; c++) {
                        let d = getColorDistance(p, centroids[c]);
                        if (d < closestDist) { closestDist = d; closestIdx = c; }
                    }
                    assignments[closestIdx].r += p[0];
                    assignments[closestIdx].g += p[1];
                    assignments[closestIdx].b += p[2];
                    assignments[closestIdx].count++;
                }
                let changed = false;
                for (let c = 0; c < k; c++) {
                    if (assignments[c].count > 0) {
                        const newR = Math.round(assignments[c].r / assignments[c].count);
                        const newG = Math.round(assignments[c].g / assignments[c].count);
                        const newB = Math.round(assignments[c].b / assignments[c].count);
                        if (newR !== centroids[c][0]) { centroids[c] = [newR, newG, newB]; changed = true; }
                    }
                }
                if (!changed) break;
            }
            return centroids;
        }

        function generateRecipe(targetRgb) {
            const distToPaper = getColorDistance(targetRgb, currentPaperRGB);
            if (distToPaper < 25) { return { type: 'paper', dist: distToPaper }; }

            const baseMatch = findClosestPencil(targetRgb);
            const basePencil = baseMatch.pencil;

            if (baseMatch.dist < 30) {
                return { type: 'single', base: basePencil, finalDist: baseMatch.dist };
            }

            let bestMixDist = baseMatch.dist;
            let bestBlendPencil = null;

            // This loop strictly iterates the 36-set prismacolorDB.
            // No pencils outside this specific set will be selected for blending.
            for (let candidate of prismacolorDB) {
                if (candidate.id === basePencil.id) continue;
                const mixR = (basePencil.rgb[0] * 0.6 + candidate.rgb[0] * 0.4);
                const mixG = (basePencil.rgb[1] * 0.6 + candidate.rgb[1] * 0.4);
                const mixB = (basePencil.rgb[2] * 0.6 + candidate.rgb[2] * 0.4);
                const dist = getColorDistance(targetRgb, [mixR, mixG, mixB]);
                
                if (dist < bestMixDist) {
                    bestMixDist = dist;
                    bestBlendPencil = candidate;
                }
            }
            return { type: 'blend', base: basePencil, blend: bestBlendPencil, finalDist: bestMixDist };
        }

        function updatePaperSettings() {
            const select = els.paperTypeSelect;
            const option = select.options[select.selectedIndex];
            
            if (select.value === 'custom') {
                els.customPaperPicker.disabled = false;
                els.customPaperPicker.classList.remove('opacity-50');
                const hex = els.customPaperPicker.value;
                currentPaperRGB = hexToRgb(hex);
                currentPaperName = "Custom Surface";
                els.paperPreview.style.backgroundColor = hex;
            } else {
                els.customPaperPicker.disabled = true;
                els.customPaperPicker.classList.add('opacity-50');
                const hex = option.dataset.color;
                currentPaperRGB = hexToRgb(hex);
                currentPaperName = option.text;
                els.paperPreview.style.backgroundColor = hex;
                els.customPaperPicker.value = hex; 
            }
            if (currentImage) analyzeImage();
        }

        function handleImageUpload(e) {
            const file = e.target.files[0] || e.dataTransfer.files[0];
            if (!file) return;
            currentFileName = file.name.replace(/\.[^/.]+$/, "");
            els.fileNameDisplay.textContent = file.name;

            const reader = new FileReader();
            reader.onload = (event) => {
                const img = new Image();
                img.onload = () => {
                    currentImage = img;
                    setupCanvas();
                    els.uploadPrompt.classList.add('hidden');
                    els.canvasContainer.classList.remove('hidden');
                    els.resetBtn.classList.remove('hidden');
                    els.instructionText.classList.remove('hidden');
                    analyzeImage();
                };
                img.src = event.target.result;
            };
            reader.readAsDataURL(file);
        }

        function setupCanvas() {
            if (!currentImage) return;
            const maxDimension = 3840; 
            let w = currentImage.width;
            let h = currentImage.height;
            if (w > maxDimension || h > maxDimension) {
                const ratio = Math.min(maxDimension / w, maxDimension / h);
                w *= ratio;
                h *= ratio;
            }
            els.canvas.width = w;
            els.canvas.height = h;
            ctx.drawImage(currentImage, 0, 0, w, h);
        }

        function analyzeImage() {
            if (!currentImage) return;
            const k = parseInt(els.countInput.value);
            els.downloadBtn.disabled = true;
            els.copyBtn.disabled = true;
            els.aiGuideBtn.disabled = true;

            setTimeout(() => {
                const tempCanvas = document.createElement('canvas');
                const tempCtx = tempCanvas.getContext('2d');
                tempCanvas.width = 150;
                tempCanvas.height = 150 * (currentImage.height / currentImage.width);
                tempCtx.drawImage(currentImage, 0, 0, tempCanvas.width, tempCanvas.height);
                const smallImgData = tempCtx.getImageData(0, 0, tempCanvas.width, tempCanvas.height);

                const dominantColors = extractPalette(smallImgData, k);
                const uniqueItems = new Set();
                
                dominantColors.forEach(rgb => {
                    const distToPaper = getColorDistance(rgb, currentPaperRGB);
                    if (distToPaper < 30) {
                        uniqueItems.add(JSON.stringify({ type: 'paper' }));
                    } else {
                        const match = findClosestPencil(rgb).pencil;
                        uniqueItems.add(JSON.stringify({ type: 'pencil', data: match }));
                    }
                });

                activePencilSet = Array.from(uniqueItems).map(JSON.parse);
                activePencilSet.sort((a, b) => {
                    if (a.type === 'paper') return -1;
                    if (b.type === 'paper') return 1;
                    const briA = (a.data.rgb[0] + a.data.rgb[1] + a.data.rgb[2]);
                    const briB = (b.data.rgb[0] + b.data.rgb[1] + b.data.rgb[2]);
                    return briB - briA;
                });

                renderPencilList(activePencilSet);
                els.downloadBtn.disabled = false;
                els.copyBtn.disabled = false;
                els.aiGuideBtn.disabled = false;
            }, 50);
        }

        function renderPencilList(items) {
            els.pencilList.innerHTML = '';
            const paperHex = els.paperPreview.style.backgroundColor;

            items.forEach(item => {
                const card = document.createElement('div');
                
                if (item.type === 'paper') {
                    card.className = "flex items-center p-3 rounded-lg border-2 border-dashed border-slate-600 mb-2 opacity-75";
                    card.style.backgroundColor = paperHex;
                    const brightness = (currentPaperRGB[0]*299 + currentPaperRGB[1]*587 + currentPaperRGB[2]*114)/1000;
                    const txtColor = brightness > 125 ? 'black' : 'white';
                    card.innerHTML = `
                        <div class="w-8 h-8 rounded-full border border-current mr-3 flex-shrink-0 flex items-center justify-center">
                            <i class="fas fa-ban text-xs"></i>
                        </div>
                        <div class="flex-1 min-w-0" style="color: ${txtColor}">
                            <h3 class="font-bold text-xs uppercase tracking-wider">Negative Space</h3>
                            <p class="text-xs opacity-80">Leave as Paper Tone</p>
                        </div>
                    `;
                } else {
                    const pencil = item.data;
                    const rgbStr = `rgb(${pencil.rgb.join(',')})`;
                    
                    const displayVal = getPencilValue(pencil);

                    card.className = "pencil-card flex items-center p-2 rounded-lg border border-slate-700/50 mb-2 cursor-pointer relative overflow-hidden";
                    card.style.background = `linear-gradient(90deg, #1e293b 80%, ${paperHex} 100%)`;
                    card.innerHTML = `
                        <div class="w-8 h-8 rounded-full border border-white/20 mr-3 flex-shrink-0 shadow-sm" style="background-color: ${rgbStr}"></div>
                        <div class="flex-1 min-w-0 z-10">
                            <div class="flex justify-between items-baseline">
                                <h3 class="font-mono text-indigo-300 text-xs font-bold">${displayVal}</h3>
                            </div>
                            <p class="text-slate-300 text-xs truncate font-medium">${pencil.name}</p>
                        </div>
                    `;
                }
                els.pencilList.appendChild(card);
            });
        }

        // --- GEMINI API INTEGRATION ---
        
        async function generateAIAdvice() {
            if(!activePencilSet || activePencilSet.length === 0) return;

            els.aiModal.classList.remove('hidden');
            els.aiContent.classList.add('hidden');
            els.aiLoading.classList.remove('hidden');

            try {
                const tempCanvas = document.createElement('canvas');
                const ctx = tempCanvas.getContext('2d');
                const scale = Math.min(1, 512 / currentImage.width); 
                tempCanvas.width = currentImage.width * scale;
                tempCanvas.height = currentImage.height * scale;
                ctx.drawImage(currentImage, 0, 0, tempCanvas.width, tempCanvas.height);
                const base64Image = tempCanvas.toDataURL('image/jpeg', 0.8).split(',')[1];

                const pencilNames = activePencilSet
                    .filter(i => i.type === 'pencil')
                    .map(i => `${i.data.id} (${i.data.name})`)
                    .join(', ');

                const systemPrompt = "You are a Master Colored Pencil Artist specializing in Prismacolor Premier pencils. You must ONLY recommend colors from the standard 36-count box set. Never mention colors outside this set.";
                const userPrompt = `I am drawing this image on ${currentPaperName}. 
                My available palette matches (from the 36-set) are: ${pencilNames}.
                Please provide a 5-step tutorial on how to draw the main subject of this image using ONLY my available colors from the Prismacolor 36-count set.
                Format as Markdown.`;

                const response = await fetch(`https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash-preview-09-2025:generateContent?key=${apiKey}`, {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({
                        contents: [{
                            parts: [
                                { text: userPrompt },
                                { inlineData: { mimeType: "image/jpeg", data: base64Image } }
                            ]
                        }],
                        systemInstruction: { parts: [{ text: systemPrompt }] }
                    })
                });

                if (!response.ok) throw new Error("AI request failed");

                const result = await response.json();
                const aiText = result.candidates?.[0]?.content?.parts?.[0]?.text || "Could not generate advice.";

                els.aiContent.innerHTML = marked.parse(aiText);
                els.aiLoading.classList.add('hidden');
                els.aiContent.classList.remove('hidden');

            } catch (error) {
                console.error(error);
                els.aiLoading.classList.add('hidden');
                els.aiContent.classList.remove('hidden');
                els.aiContent.innerHTML = `<p class="text-red-400">Sorry, I couldn't generate the guide right now. Please try again.</p>`;
            }
        }

        // --- EVENTS ---

        els.displayModeInputs.forEach(radio => {
            radio.addEventListener('change', (e) => {
                currentDisplayMode = e.target.value;
                if(currentImage) renderPencilList(activePencilSet);
            });
        });

        els.canvas.addEventListener('click', (e) => {
            const rect = els.canvas.getBoundingClientRect();
            const scaleX = els.canvas.width / rect.width;
            const scaleY = els.canvas.height / rect.height;
            const x = Math.floor((e.clientX - rect.left) * scaleX);
            const y = Math.floor((e.clientY - rect.top) * scaleY);
            
            const p = ctx.getImageData(x, y, 1, 1).data;
            const targetRgb = [p[0], p[1], p[2]];

            els.targetRgbText.textContent = `RGB(${targetRgb.join(',')})`;
            els.targetColorPreview.style.backgroundColor = `rgb(${targetRgb.join(',')})`;

            const recipe = generateRecipe(targetRgb);
            
            let html = '';
            
            if (recipe.type === 'paper') {
                html = `
                    <div class="bg-slate-800/50 rounded p-3 border border-slate-600 border-dashed text-center">
                        <div class="w-10 h-10 mx-auto rounded-full mb-2 border border-slate-500" style="background-color: ${els.paperPreview.style.backgroundColor}"></div>
                        <p class="text-indigo-300 font-bold text-sm">Use Paper Tone</p>
                        <p class="text-slate-400 text-[10px]">Pixel matches background surface.</p>
                    </div>
                `;
            } else {
                const baseVal = getPencilValue(recipe.base);
                
                html += `
                    <div class="bg-slate-800/50 rounded p-2 flex items-center gap-3 border border-indigo-500/30">
                        <div class="w-8 h-8 rounded-sm shadow-sm" style="background-color: rgb(${recipe.base.rgb.join(',')})"></div>
                        <div>
                            <span class="text-[10px] uppercase font-bold text-indigo-400 block mb-0.5">Base Layer</span>
                            <p class="text-sm font-bold text-white leading-tight">${baseVal} ${recipe.base.name}</p>
                        </div>
                    </div>
                `;

                if (recipe.type === 'blend') {
                    const blendVal = getPencilValue(recipe.blend);
                    html += `<div class="text-center text-slate-500 text-xs my-[-4px]"><i class="fas fa-plus"></i></div>`;
                    html += `
                        <div class="bg-slate-800/50 rounded p-2 flex items-center gap-3 border border-slate-700">
                            <div class="w-8 h-8 rounded-sm shadow-sm" style="background-color: rgb(${recipe.blend.rgb.join(',')})"></div>
                            <div>
                                <span class="text-[10px] uppercase font-bold text-slate-400 block mb-0.5">Blend (from 36 set)</span>
                                <p class="text-sm font-bold text-slate-200 leading-tight">${blendVal} ${recipe.blend.name}</p>
                            </div>
                        </div>
                    `;
                }
            }
            els.recipeSteps.innerHTML = html;
            els.recipePopup.classList.remove('hidden');
            els.instructionText.classList.add('hidden');
        });

        els.closeRecipe.addEventListener('click', () => els.recipePopup.classList.add('hidden'));

        els.paperTypeSelect.addEventListener('change', updatePaperSettings);
        els.customPaperPicker.addEventListener('input', updatePaperSettings);
        els.resetBtn.addEventListener('click', () => location.reload());
        
        els.dropZone.addEventListener('click', (e) => {
            if (els.uploadPrompt.contains(e.target)) els.fileInput.click();
        });
        els.fileInput.addEventListener('change', handleImageUpload);
        ['dragenter', 'dragover', 'dragleave', 'drop'].forEach(n => {
            els.dropZone.addEventListener(n, (e) => { e.preventDefault(); e.stopPropagation(); }, false);
        });
        els.dropZone.addEventListener('drop', handleImageUpload);
        
        els.countInput.addEventListener('input', (e) => els.countDisplay.textContent = `${e.target.value} Pencils`);
        els.countInput.addEventListener('change', analyzeImage);
        window.addEventListener('resize', setupCanvas);

        els.downloadBtn.addEventListener('click', () => {
            if (activePencilSet.length === 0) return;
            let fileContent = `Prismacolor Palette for: ${currentFileName}\n`;
            fileContent += `Set: 36 Count Premier\n`;
            fileContent += `Paper Surface: ${currentPaperName}\n`;
            fileContent += `Mode: ${currentDisplayMode.toUpperCase()}\n`;
            fileContent += `Generated: ${new Date().toLocaleDateString()}\n`;
            fileContent += `----------------------------------------\n`;
            activePencilSet.forEach(p => {
                if(p.type === 'pencil') {
                    const val = getPencilValue(p.data);
                    fileContent += `[ ] ${val} - ${p.data.name}\n`;
                } else {
                    fileContent += `[ ] (Negative Space) - Use Paper Tone\n`;
                }
            });
            fileContent += `----------------------------------------\n`;
            const blob = new Blob([fileContent], { type: 'text/plain' });
            const url = URL.createObjectURL(blob);
            const a = document.createElement('a');
            a.href = url;
            a.download = `${currentFileName}_36set_palette.txt`;
            document.body.appendChild(a);
            a.click();
            document.body.removeChild(a);
        });

        els.copyBtn.addEventListener('click', () => {
            const text = activePencilSet.map(p => {
                if (p.type === 'pencil') {
                    const val = getPencilValue(p.data);
                    return `- [ ] ${val}: ${p.data.name}`;
                }
                return `- [ ] Negative Space (Paper Tone)`;
            }).join('\n');
            navigator.clipboard.writeText(`Prismacolor 36-Set List (${currentPaperName}):\n${text}`);
        });

        // AI Events
        els.aiGuideBtn.addEventListener('click', generateAIAdvice);
        els.closeAiModal.addEventListener('click', () => els.aiModal.classList.add('hidden'));

        updatePaperSettings();

    </script>
</body>
</html>
