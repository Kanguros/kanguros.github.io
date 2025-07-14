---
title: Quick enhacements of Github Copilot
date: 2025-07-14
summary: How I enhance my Github Copilot capabilities using Chat Modes and Prompts.
---

[TOC]

## Script for Chat Modes & Prompts

Script below pulls Chat Modes and Prompts from the official Microsoft repository for Copilot (https://github.com/github/awesome-copilot.git) to your VS Code.

You get 30+ specialized Agents for different tasks like debugging, code review, architecture planning, and more. Everything installs globally and works in all your projects.

### How to use

1. Copy and paste the script to PowerShell terminal
2. Restart VS Code
3. Open Copilot Chat - you'll see all the new modes in the dropdown

### What you get

- _Chat Modes_: Specialized Agents. (Debug Mode, API Architect, Security Scout, etc.)
- _Prompts_: Reusable templates for common tasks.

```powershell

$repoUrl = 'https://github.com/github/awesome-copilot.git'
$localRepoPath = ".\copilot-chatmodes"
$vsCodeUserPromptsPath = "$env:APPDATA\Code\User\prompts"

if (Test-Path $localRepoPath) {
    Write-Host "Repository exists. Pulling latest changes..."
    Set-Location $localRepoPath
    git pull
    Set-Location ..
} else {
    Write-Host "Cloning repository..."
    git clone $repoUrl $localRepoPath
}

if (-Not (Test-Path $vsCodeUserPromptsPath)) {
    New-Item -ItemType Directory -Path $vsCodeUserPromptsPath | Out-Null
}

Write-Host "Copying Chatmodes files..."
Copy-Item -Path "$localRepoPath\chatmodes\*.chatmode.md" -Destination $vsCodeUserPromptsPath -Force
Write-Host "Copying Prompts files..."
Copy-Item -Path "$localRepoPath\prompts\*.prompt.md" -Destination $vsCodeUserPromptsPath -Force
Write-Host "Installation complete. Restart VS Code to activate."

```

## Master Chatmode Generator

The Master Chatmode Generator is a specialized AI assistant that creates custom GitHub Copilot chat modes for any subject or domain. Instead of manually writing chat mode files, you simply tell it what you need and it generates a complete, ready-to-use .chatmode.md file.

### How to use

1. Save the Master Generator as `Master Prompt.chatmode.md` in your `$env:APPDATA\Code\User\prompts`
2. Restart VS Code
3. Select "Master Prompt" from Copilot Chat dropdown
4. Type your subject:
    - Create a chatmode for Python testing
    - Generate a chatmode for API documentation
5. Copy the generated output and save it as a new .chatmode.md file
