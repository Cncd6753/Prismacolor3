import streamlit as st
import streamlit.components.v1 as components

# Set the page layout to wide to accommodate the 16:9 format preference
st.set_page_config(layout="wide", page_title="Prismacolor Master - 36 Set")

# Embed the full HTML/JS/CSS application code here
# We use r""" (raw string) to ensure Python ignores backslashes in the JavaScript regex
html_app = r"""
<!DOCTYPE html>
<html lang="en" class="dark">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Prismacolor Master - 36 Set Edition</title>
    
    <!-- Tailwind with Dark Mode Config -->
    <script src="https://cdn.tailwindcss.com"></script>
    <script>
        tailwind.config = {
            darkMode: 'class',
            theme: {
                extend: {
                    colors: {
                        slate: {
                            850: '#151e2e',
                        }
                    }
                }
            }
        }
    </script>
    
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css" rel="stylesheet">
    <script src="https://cdn.jsdelivr.net/npm/marked/marked.min.js"></script>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&display=swap');
        
        :root {
            --grid-color-1: #e2e8f0; /* Light mode grid color */
            --grid-color-2: transparent;
        }

        .dark {
            --grid-color-1: #1e293b; /* Dark mode grid color */
        }

        body {
            font-family: 'Inter', sans-serif;
            overflow: hidden;
            height: 100vh;
            width: 100vw;
            transition: background-color 0.3s, color 0.3s;
            margin: 0;
            padding: 0;
        }

        /* Glass Panel Effect - Adaptive */
        .glass-panel {
            background: rgba(255, 255, 255, 0.95);
            backdrop-filter: blur(12px);
            border: 1px solid rgba(0, 0, 0, 0.1);
        }
        .dark .glass-panel {
            background: rgba(15, 23, 42, 0.95);
            border: 1px solid rgba(255, 255, 255, 0.1);
        }

        /* Interactive Elements */
        .pencil-card {
            transition: all 0.2s ease;
        }
        .pencil-card:hover {
            transform: translateX(4px);
            filter: brightness(0.95);
        }
        .dark .pencil-card:hover {
            filter: brightness(1.1);
        }

        /* Canvas Background Grid - Uses CSS Variables for Theming */
        .canvas-wrapper {
            box-shadow: 0 20px 50px -10px rgba(0, 0, 0, 0.2);
            cursor: crosshair;
            display: flex;
            align-items: center;
            justify-content: center;
            width: 100%;
            height: 100%;
            overflow: hidden;
            background-image: 
                linear-gradient(45deg, var(--grid-color-1) 25%, transparent 25%), 
                linear-gradient(-45deg, var(--grid-color-1) 25%, transparent 25%), 
                linear-gradient(45deg, transparent 75%, var(--grid-color-1) 75%), 
                linear-gradient(-45deg, transparent 75%, var(--grid-color-1) 75%);
            background-size: 20px 20px;
            background-position: 0 0, 0 10px, 10px -10px, -10px 0px;
            transition: background-image 0.3s;
        }
        .dark .canvas-wrapper {
            box-shadow: 0 20px 50px -10px rgba(0, 0, 0, 0.7);
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
        input[type="color"]::-webkit-color-swatch { border: 2px solid #cbd5e1; border-radius: 50%; }
        .dark input[type="color"]::-webkit-color-swatch { border: 2px solid #475569; }

        /* Custom Radio Buttons */
        .radio-label {
            cursor: pointer;
            display: flex;
            align-items: center;
            gap: 0.5rem;
            font-size: 0.75rem;
            color: #64748b; /* Light mode text */
            transition: color 0.2s;
        }
        .dark .radio-label { color: #94a3b8; }
        
        .radio-label:hover { color: #0f172a; }
        .dark .radio-label:hover { color: #e2e8f0; }

        .radio-input {
            appearance: none;
            background-color: #f1f5f9;
            margin: 0;
            font: inherit;
            color: currentColor;
            width: 1.15em;
            height: 1.15em;
            border: 1px solid #cbd5e1;
            border-radius: 50%;
            display: grid;
            place-content: center;
        }
        .dark .radio-input {
            background-color: #1e293b;
            border: 1px solid #475569;
        }

        .radio-input::before {
            content: "";
            width: 0.65em;
            height: 0.65em;
            border-radius: 50%;
            transform: scale(0);
            transition: 120ms transform ease-in-out;
            box-shadow: inset 1em 1em #6366f1; /* Indigo */
        }
        .radio-input:checked::before { transform: scale(1); }
        .radio-input:checked + span { color: #4f46e5; font-weight: 600; }
        .dark .radio-input:checked + span { color: #818cf8; }

        ::-webkit-scrollbar { width: 6px; height: 6px; }
        ::-webkit-scrollbar-track { background: #f1f5f9; }
        .dark ::-webkit-scrollbar-track { background: #0f172a; }
        
        ::-webkit-scrollbar-thumb { background: #cbd5e1; border-radius: 3px; }
        .dark ::-webkit-scrollbar-thumb { background: #334155; }
        
        ::-webkit-scrollbar-thumb:hover { background: #94a3b8; }
        .dark ::-webkit-scrollbar-thumb:hover { background: #475569; }

        .recipe-card { animation: slideIn 0.3s cubic-bezier(0.16, 1, 0.3, 1); }
        @keyframes slideIn {
            from { opacity: 0; transform: translateY(20px) scale(0.95); }
            to { opacity: 1; transform: translateY(0) scale(1); }
        }

        /* Markdown Styling */
        .prose h3 { color: #4f46e5; font-weight: bold; margin-top: 1em; margin-bottom: 0.5em; }
        .dark .prose h3 { color: #818cf8; }
        
        .prose ul { list-style-type: disc; padding-left: 1.5em; color: #334155; }
        .dark .prose ul { color: #cbd5e1; }
        
        .prose li { margin-bottom: 0.5em; }
        
        .prose strong { color: #0f172a; }
        .dark .prose strong { color: #e2e8f0; }
        
        .prose p { margin-bottom: 0.8em; line-height: 1.6; color: #475569; }
        .dark .prose p { color: #94a3b8; }
    </style>
</head>
<body class="flex flex-col h-screen w-screen overflow-hidden bg-slate-50 dark:bg-slate-950 text-slate-800 dark:text-e2e8f0 transition-colors duration-300">

    <!-- Header -->
    <header class="h-14 bg-white/90 dark:bg-slate-900/90 border-b border-slate-200 dark:border-slate-700/50 flex items-center justify-between px-6 flex-shrink-0 z-20 backdrop-blur-sm transition-colors duration-300">
        <div class="flex items-center gap-3">
            <i class="fas fa-layer-group text-indigo-600 dark:text-indigo-500 text-xl"></i>
            <h1 class="text-lg font-bold tracking-wide text-slate-800 dark:text-slate-100">Prisma<span class="text-indigo-500 dark:text-indigo-400">Board</span> 36 Set</h1>
        </div>
        <div class="flex items-center gap-4">
            <span id="fileNameDisplay" class="text-xs font-mono text-slate-500 dark:text-slate-400 hidden md:block"></span>
            
            <!-- Theme Toggle -->
            <button id="themeToggle" class="w-8 h-8 rounded-full flex items-center justify-center bg-slate-100 dark:bg-slate-800 text-slate-600 dark:text-yellow-400 hover:bg-slate-200 dark:hover:bg-slate-700 transition-colors" title="Toggle Day/Night Mode">
                <i class="fas fa-moon dark:hidden"></i>
                <i class="fas fa-sun hidden dark:block"></i>
            </button>

            <button id="resetBtn" class="bg-slate-200 hover:bg-slate-300 dark:bg-slate-800 dark:hover:bg-slate-700 text-slate-700 dark:text-white px-3 py-1.5 rounded text-xs font-medium transition hidden border border-slate-300 dark:border-slate-600">
                New Project
            </button>
        </div>
    </header>

    <!-- Main Layout -->
    <main class="flex-1 flex flex-col lg:flex-row overflow-hidden relative h-full">
        
        <!-- CANVAS AREA (Left) -->
        <section class="flex-1 bg-slate-100 dark:bg-slate-950 relative flex flex-col items-center justify-center p-4 overflow-hidden h-full transition-colors duration-300" id="dropZone">
            
            <!-- Upload UI -->
            <div id="uploadPrompt" class="text-center p-16 border-2 border-dashed border-slate-300 dark:border-slate-700/50 rounded-2xl hover:border-indigo-500/50 hover:bg-slate-200/50 dark:hover:bg-slate-900/30 transition cursor-pointer group">
                <div class="w-20 h-20 bg-slate-200 dark:bg-slate-900 rounded-full flex items-center justify-center mx-auto mb-6 group-hover:scale-110 transition duration-300 shadow-xl shadow-black/10 dark:shadow-black/50">
                    <i class="fas fa-image text-3xl text-indigo-500 dark:text-indigo-400"></i>
                </div>
                <h2 class="text-2xl font-semibold mb-2 text-slate-700 dark:text-slate-200">Drop Reference Image</h2>
                <p class="text-slate-500 dark:text-slate-500 mb-6 text-sm">Strictly matched to the 36-count box.</p>
                <button class="bg-indigo-600 hover:bg-indigo-500 text-white px-8 py-3 rounded-full font-medium shadow-lg shadow-indigo-900/20 transition hover:shadow-indigo-600/30">
                    Select File
                </button>
                <input type="file" id="fileInput" accept="image/*" class="hidden">
            </div>

            <!-- Canvas Wrapper -->
            <div id="canvasContainer" class="hidden canvas-wrapper rounded-lg border border-slate-200 dark:border-slate-800 bg-white dark:bg-slate-900 w-full h-full relative">
                <canvas id="mainCanvas"></canvas>
                
                <!-- Hover Tooltip -->
                <div id="hoverTooltip" class="fixed pointer-events-none bg-white/90 dark:bg-black/80 border border-slate-200 dark:border-white/10 text-slate-800 dark:text-white text-xs rounded-md px-2 py-1 hidden z-50 backdrop-blur-sm whitespace-nowrap shadow-lg">
                    <span id="hoverCoords"></span>
                </div>

                <!-- Color Recipe Popup -->
                <div id="recipePopup" class="absolute bottom-4 right-4 w-72 glass-panel rounded-xl p-4 hidden recipe-card shadow-2xl z-40 border-l-4 border-indigo-500">
                    <div class="flex justify-between items-start mb-3">
                        <h3 class="text-sm font-bold text-slate-800 dark:text-white uppercase tracking-wider"><i class="fas fa-flask mr-2"></i>36-Set Recipe</h3>
                        <button id="closeRecipe" class="text-slate-400 hover:text-slate-600 dark:hover:text-white"><i class="fas fa-times"></i></button>
                    </div>
                    
                    <div class="flex items-center gap-3 mb-4">
                        <div id="targetColorPreview" class="w-12 h-12 rounded-full border-2 border-slate-200 dark:border-white/20 shadow-inner"></div>
                        <div class="text-xs text-slate-500 dark:text-slate-300">
                            <p>Target Pixel</p>
                            <p class="font-mono text-[10px] opacity-70" id="targetRgbText">RGB(0,0,0)</p>
                        </div>
                    </div>

                    <div class="space-y-3" id="recipeSteps">
                        <!-- Dynamic Content injected here -->
                    </div>
                </div>
            </div>
            
            <div id="instructionText" class="absolute bottom-6 text-slate-500 dark:text-slate-500 text-xs hidden animate-pulse pointer-events-none bg-white/80 dark:bg-slate-900/50 px-3 py-1 rounded shadow-sm">
                <i class="fas fa-mouse-pointer mr-2"></i>Click image to see layering recipe
            </div>

        </section>

        <!-- SIDEBAR (Right) -->
        <aside class="w-full lg:w-[420px] bg-white dark:bg-slate-900 border-l border-slate-200 dark:border-slate-800 flex flex-col z-10 shadow-2xl h-full overflow-hidden transition-colors duration-300">
            
            <div class="flex-shrink-0">
                <!-- Paper Settings -->
                <div class="p-5 border-b border-slate-200 dark:border-slate-800 bg-white dark:bg-slate-900 transition-colors">
                    <h2 class="text-xs font-bold uppercase tracking-widest text-indigo-600 dark:text-indigo-400 mb-3 flex items-center gap-2">
                        <i class="fas fa-scroll"></i> Paper / Surface
                    </h2>
                    
                    <div class="grid grid-cols-[1fr_auto] gap-3 mb-3">
                        <select id="paperTypeSelect" class="bg-slate-50 dark:bg-slate-800 border border-slate-300 dark:border-slate-700 text-slate-700 dark:text-white text-sm rounded-lg focus:ring-
