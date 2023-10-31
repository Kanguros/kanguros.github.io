Title: Variables and parameters in Azure Pipeline  
Date: 2023-07-15   
Tags: azure_pipeline, parameters, variables  
Category: Article  
Summary: Short and brief information about **variables** and **parameters** in **Azure Pipeline**.

## Variables

- Used to **store and manage data** during the pipeline execution.
- Value **can only be string**.
- Are **mutable** and value can change from run to run or job to job.
- Can be overwrite, the most locally scoped variable wins.

### Definition example

```yaml
variables:
 - name: myImportantVariable
   value: contoso
 - name: SECONDVARIABLE
   value: "LongTextPRDEnv"
```

### Usage example

```yaml
steps: 
- bash: echo $(myImportantVariable)
- powershell: echo $(myImportantVariable)
- script: echo $(myImportantVariable)
```

## Parameters

- Used to **provide input values** to a pipeline when it is triggered.
- Value could be string, number, bool or object (and more complex types).
- Can only be used in **template expressions**.

### Definition example

```yaml
parameters:
- name: myString
  type: string
  default: a string
  
- name: myMultiString
  type: string
  default: default
  values:
  - default
  - ubuntu
```

```yaml
parameters:
- name: myNumber
  type: number
  default: 2
  values:
  - 1
  - 2
  - 16

- name: myBoolean
  type: boolean
  default: true
  
- name: myObject
  type: object
  default:
    foo: FOO
    bar: BAR
    things:
    - one
    - two
    nested:
      one: apple
      two: pear
      count: 3
```

All available data types could be found in [Azure documentation](https://learn.microsoft.com/en-us/azure/devops/pipelines/process/template-parameters?view=azure-devops#parameter-data-types)

### Usage example

```yaml
parameters:
- name: image
  displayName: Pool Image
  type: string
  default: ubuntu-latest
  values:
  - windows-latest
  - ubuntu-latest
  - macOS-latest

trigger: none

jobs:
- job: build
  displayName: build
  pool: 
    vmImage: ${{ parameters.image }}
  steps:
  - script: echo building $(Build.BuildNumber) with ${{ parameters.image }}
```

##  How to use it

It depends ;) 

First of all, we need to know that there are 3 different syntaxes for using a variables and parameters. 

### Syntax

A syntax how the variable or parameter is referenced, determines when the value will be processed. 

| Type              | Example                | When is it processed?          |
| ------------------- | ---------------------- | ------------------------------ |
| template expression | `${{ variables.var }}` | compile time |
| macro               | `$(var)`               | runtime before a task executes |
| runtime expression  | `$[variables.var]`     | runtime      |

### Template expression

- Are **process at compile time**, and get replaced before runtime starts. 
- Are designed for reusing parts of YAML as templates.

### Macro

...
## Runtime expression

...