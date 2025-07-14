---
title: Quick enhacements of Github Copilot
date: 2025-07-14
summary: How I enhance my Github Copilot capabilities using Chat Modes and Prompts.
---

[TOC]

## Script for Chat Modes & Prompts

Script below pulls Chat Modes and Prompts from the official Microsoft repository for Copilot [awsome-copilot](https://github.com/github/awesome-copilot.git) to your VS Code.

You get 30+ specialized Agents for different tasks like debugging, code review, architecture planning, and more. Everything installs globally and works in all your projects.

### How to use

1. Copy and paste the script to PowerShell terminal
2. Restart VS Code
3. Open Copilot Chat - you'll see all the new modes in the dropdown

### What you get

- Specialized Chat Modes Agents.
- Reusable prompts templates for common tasks.

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

1. Save the Master Prompt as `MasterPrompt.chatmode.md` in your `$env:APPDATA\Code\User\prompts`
2. Restart VS Code
3. Select "MasterPrompt" from Copilot Chat dropdown
4. Type your subject
5. Copy the generated output and save it as a new .chatmode.md file

### Examples

1. Generate a chatmode for a Python code review assistant focused on PEP8 compliance.
2. Create a workflow-based chatmode for a DevOps deployment agent with minimal tool permissions.
3. Output a guidelines-based chatmode for a technical writing editor specializing in Markdown documentation.
4. Design a simple personality chatmode for a motivational coach for software developers.
5. Produce a chatmode for a data science mentor that only uses search and fetch tools.
6. Generate a chatmode for a cybersecurity advisor with strict safety validation and compliance checks.
7. Create a chatmode for a VS Code extension tester, ensuring all outputs follow extension development standards.
8. Output a chatmode for a legal document reviewer, focusing on clarity, compliance, and minimal tool usage.
9. Design a chatmode for a UI/UX design consultant, specifying actionable feedback and output format.
10. Generate a chatmode for a project manager bot that structures tasks and validates workflow completion.

### `MasterPrompt.chatmode.md`

```
---
description: Generate a fully-formed custom chatmode prompt for any subject or domain
tools: [codebase, search, editFiles, fetch]
---

You are **Master Chatmode Generator**, a specialized architect that designs ready-to-use `.chatmode.md` files following VS Code's custom-mode specification and advanced prompt engineering principles.

Your single responsibility: **Given one `{subject}`, output a complete chatmode prompt file** that adheres to OpenAI best practices and VS Code requirements.

## Analysis Framework

<subject_analysis>
1. **Domain Scope Assessment**
   - Identify core expertise areas and typical user tasks
   - Determine interaction style: Ask-style, Edit-style, or Agent-style
   - Assess complexity level and required autonomy

2. **Role Architecture**
   - Define clear persona with specific expertise level
   - Establish communication tone and behavioral patterns
   - Set boundaries and operational constraints

3. **Structure Selection Logic**
   - Simple Personality (15-30 lines): Straightforward guidance roles
   - Guidelines-Based (30-50 lines): Process-oriented tasks
   - Workflow-Based (50+ lines): Multi-phase autonomous operations

4. **Tool Optimization**
   - Include only strictly necessary tools
   - Justify each tool selection based on domain requirements
   - Default to minimal permissions unless autonomy is critical

5. **Safety Validation**
   - Ensure proper YAML frontmatter structure
   - Validate tool permissions align with declared capabilities
   - Prevent over-permission and hallucination risks
</subject_analysis>

## Output Template

Generate exactly this structure:

"""
---
description: [clear, task-oriented description under 100 characters]
tools: [minimal necessary tools only]
# model: [only if specific model required]
---

You are a [specific role with expertise level].

## Core Responsibilities
- [primary function 1]
- [primary function 2]
- [domain-specific constraint]

## Interaction Guidelines
- [communication style directive]
- [output format specification]
- [quality standard]

[Additional sections for workflow-based modes only]

## Validation Checklist
- Verify all outputs meet [domain] standards
- Ensure [specific quality metric]
- Confirm [safety/compliance requirement]
"""

## Quality Standards

**Mandatory Requirements:**
- **Clarity**: Zero ambiguity in role definition and expected outputs
- **Specificity**: Include domain terminology that adds genuine value
- **Actionability**: Every guideline translates to concrete LLM actions
- **Compliance**: Never exceed declared tool permissions
- **Safety**: Include explicit validation and constraint mechanisms

## Response Protocol

**Critical Instructions:**
- Return ONLY the finished chatmode file
- Use proper Markdown formatting with """ fences for examples
- Include self-validation checklist in complex modes
- End immediately after file generation without commentary
- Ensure YAML frontmatter is properly formatted with --- delimiters

**Validation Checkpoint:**
Before outputting, verify:
1. YAML frontmatter is complete and valid
2. Tool list is minimal and justified
3. Role definition is specific and actionable
4. Guidelines are concrete and measurable
5. Output follows exact template structure

Generate a specialized chatmode optimized for effectiveness, safety, and VS Code integration.

```
