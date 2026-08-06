# Triagem SonarCloud — flext-sh/flext-dbt-ldif

Gerado do dump da plataforma SonarCloud (2026-08-06).

Bead: `mro-2wjm.4`

## Resumo

**91 issues** — BLOCKER 3, CRITICAL 61, MAJOR 23, MINOR 2
Tipos: VULNERABILITY 22, BUG 0, CODE_SMELL 69 · **Debt total: 1296min**

| regra | issues |
|---|---|
| `plsql:LiteralsNonPrintableCharactersCheck` | 34 |
| `plsql:S1192` | 25 |
| `githubactions:S7637` | 6 |
| `githubactions:S8544` | 6 |
| `shelldre:S7688` | 3 |
| `githubactions:S7630` | 2 |
| `python:S1192` | 2 |
| `githubactions:S8233` | 2 |
| `githubactions:S7635` | 2 |
| `githubactions:S8541` | 2 |

## Como usar

Cada issue traz a **mensagem do SonarQube** (descreve o problema e o impacto), o **código real** (linha `>>>`), o tipo e o effort estimado.
**Decisão**: `corrigir` / `falso-positivo` (marcar na plataforma com justificativa) / `risco-aceito`. Ordem: BLOCKER → CRITICAL → VULNERABILITY → MAJOR. CODE_SMELL em volume pede correção de padrão.

## Issues

### 1 · 🔴 BLOCKER · VULNERABILITY · `githubactions:S7630`
**Local**: `dbt_packages/dbt_utils/.github/workflows/ci.yml:49` · **Effort**: 1h

> inputs.adapter is vulnerable to script injection: values of inputs are provided by whoever triggers the workflow. Change this workflow to not use user-controlled data directly in a run block, for example by assigning this expression to an environment variable.

```yaml
       45  
       46              - name: "Get list of supported adapters or use input adapter only"
       47                id: list-adapters
       48                run: |
>>>    49                    if [ -z "${{ inputs.adapter }}" ]; then
       50                        # github adds a pip freeze and a new line we need to strip out
       51                        source supported_adapters.env
       52                        echo $SUPPORTED_ADAPTERS
       53                        echo "test_adapters=$SUPPORTED_ADAPTERS" >> $GITHUB_OUTPUT
```

**Decisão**: 

### 2 · 🔴 BLOCKER · VULNERABILITY · `githubactions:S7630`
**Local**: `dbt_packages/dbt_utils/.github/workflows/ci.yml:55` · **Effort**: 1h

> inputs.adapter is vulnerable to script injection: values of inputs are provided by whoever triggers the workflow. Change this workflow to not use user-controlled data directly in a run block, for example by assigning this expression to an environment variable.

```yaml
       51                        source supported_adapters.env
       52                        echo $SUPPORTED_ADAPTERS
       53                        echo "test_adapters=$SUPPORTED_ADAPTERS" >> $GITHUB_OUTPUT
       54                    else
>>>    55                        echo "test_adapters=${{ inputs.adapter }}" >> $GITHUB_OUTPUT
       56                    fi
       57  
       58              - name: "Format adapter list for use as the matrix"
       59                id: supported-adapters
```

**Decisão**: 

### 3 · 🔴 BLOCKER · CODE_SMELL · `python:S1845`
**Local**: `src/flext_dbt_ldif/api.py:49` · **Effort**: 10min

> Rename method "service" to prevent any misunderstanding/clash with field "Service" defined on line 39

```python
       45              cls._instance = cls()
       46          return cls._instance
       47  
       48      @property
>>>    49      def service(self) -> FlextDbtLdifServiceMixin.Service:
       50          """The bound workflow service."""
       51          return self._service
       52  
       53      def execute(self) -> p.Result[FlextDbtLdifSettings]:
```

**Decisão**: 

### 4 · 🟠 CRITICAL · CODE_SMELL · `plsql:LiteralsNonPrintableCharactersCheck`
**Local**: `dbt_packages/codegen/macros/generate_model_import_ctes.sql:47` · **Effort**: 10min

> An illegal character with code point 10 was found in this literal.

```sql
       43            where each <something> is enclosed by (` or [ or " or ' or nothing)
       44  
       45          # from_table_2
       46          - matches (from or join) followed by some spaces and then <something>.<something_else>.<something_different>
>>>    47            where each <something> is enclosed by (` or [ or " or ' or nothing)
       48  
       49          # from_table_3
       50          - matches (from or join) followed by some spaces and then <something>
       51            where <something> is enclosed by (` or [ or " or ')
```

**Decisão**: 

### 5 · 🟠 CRITICAL · CODE_SMELL · `plsql:LiteralsNonPrintableCharactersCheck`
**Local**: `dbt_packages/codegen/macros/generate_model_import_ctes.sql:65` · **Effort**: 10min

> An illegal character with code point 10 was found in this literal.

```sql
       61      {%- set does_raw_sql_contain_cte = re.search(with_regex, model_raw_sql) -%}
       62  
       63      {%- set from_regexes = {
       64          'from_ref':
>>>    65              '(?ix)
       66  
       67              # first matching group
       68              # from or join followed by at least 1 whitespace character
       69              (from|join)\s+
```

**Decisão**: 

### 6 · 🟠 CRITICAL · CODE_SMELL · `plsql:LiteralsNonPrintableCharactersCheck`
**Local**: `dbt_packages/codegen/macros/generate_model_import_ctes.sql:81` · **Effort**: 10min

> An illegal character with code point 10 was found in this literal.

```sql
       77              ([^)\'\"]+)
       78              
       79              # fourth matching group
       80              # 1 or 0 quotation mark, 0 or more whitespace character(s)
>>>    81              ([\'\"]?\s*)
       82  
       83              # fifth matching group
       84              # a closing parenthesis, 0 or more whitespace character(s), closing }}
       85              (\)\s*}})
```

**Decisão**: 

### 7 · 🟠 CRITICAL · CODE_SMELL · `plsql:S1192`
**Local**: `dbt_packages/codegen/macros/generate_model_import_ctes.sql:88` · **Effort**: 4min

> Define a constant instead of duplicating this literal 4 times.

```sql
       84              # a closing parenthesis, 0 or more whitespace character(s), closing }}
       85              (\)\s*}})
       86          
       87              ',
>>>    88          'from_source':
       89              '(?ix)
       90  
       91              # first matching group
       92              # from or join followed by at least 1 whitespace character
```

**Decisão**: 

### 8 · 🟠 CRITICAL · CODE_SMELL · `plsql:LiteralsNonPrintableCharactersCheck`
**Local**: `dbt_packages/codegen/macros/generate_model_import_ctes.sql:89` · **Effort**: 10min

> An illegal character with code point 10 was found in this literal.

```sql
       85              (\)\s*}})
       86          
       87              ',
       88          'from_source':
>>>    89              '(?ix)
       90  
       91              # first matching group
       92              # from or join followed by at least 1 whitespace character
       93              (from|join)\s+
```

**Decisão**: 

### 9 · 🟠 CRITICAL · CODE_SMELL · `plsql:LiteralsNonPrintableCharactersCheck`
**Local**: `dbt_packages/codegen/macros/generate_model_import_ctes.sql:105` · **Effort**: 10min

> An illegal character with code point 10 was found in this literal.

```sql
      101              ([^)\'\"]+)
      102  
      103              # fourth matching group
      104              # 1 or 0 quotation mark, 0 or more whitespace character(s)
>>>   105              ([\'\"]?\s*)
      106  
      107              # fifth matching group
      108              # a comma
      109              (,)
```

**Decisão**: 

### 10 · 🟠 CRITICAL · CODE_SMELL · `plsql:LiteralsNonPrintableCharactersCheck`
**Local**: `dbt_packages/codegen/macros/generate_model_import_ctes.sql:121` · **Effort**: 10min

> An illegal character with code point 10 was found in this literal.

```sql
      117              ([^)\'\"]+)
      118  
      119              # eighth matching group
      120              # 1 or 0 quotation mark, 0 or more whitespace character(s)
>>>   121              ([\'\"]?\s*)
      122  
      123              # ninth matching group
      124              # a closing parenthesis, 0 or more whitespace character(s), closing }}
      125              (\)\s*}})
```

**Decisão**: 

### 11 · 🟠 CRITICAL · CODE_SMELL · `plsql:LiteralsNonPrintableCharactersCheck`
**Local**: `dbt_packages/codegen/macros/generate_model_import_ctes.sql:129` · **Effort**: 10min

> An illegal character with code point 10 was found in this literal.

```sql
      125              (\)\s*}})
      126  
      127              ',
      128          'from_var_1':
>>>   129              '(?ix)
      130  
      131              # first matching group
      132              # from or join followed by at least 1 whitespace character
      133              (from|join)\s+
```

**Decisão**: 

### 12 · 🟠 CRITICAL · CODE_SMELL · `plsql:LiteralsNonPrintableCharactersCheck`
**Local**: `dbt_packages/codegen/macros/generate_model_import_ctes.sql:145` · **Effort**: 10min

> An illegal character with code point 10 was found in this literal.

```sql
      141              ([^)\'\"]+)
      142  
      143              # fourth matching group
      144              # 1 or 0 quotation mark, 0 or more whitespace character(s)
>>>   145              ([\'\"]?\s*)
      146  
      147              # fifth matching group
      148              # a closing parenthesis, 0 or more whitespace character(s), closing }}
      149              (\)\s*}})
```

**Decisão**: 

### 13 · 🟠 CRITICAL · CODE_SMELL · `plsql:LiteralsNonPrintableCharactersCheck`
**Local**: `dbt_packages/codegen/macros/generate_model_import_ctes.sql:153` · **Effort**: 10min

> An illegal character with code point 10 was found in this literal.

```sql
      149              (\)\s*}})
      150              
      151              ',
      152          'from_var_2':
>>>   153              '(?ix)
      154  
      155              # first matching group
      156              # from or join followed by at least 1 whitespace character
      157              (from|join)\s+
```

**Decisão**: 

### 14 · 🟠 CRITICAL · CODE_SMELL · `plsql:LiteralsNonPrintableCharactersCheck`
**Local**: `dbt_packages/codegen/macros/generate_model_import_ctes.sql:169` · **Effort**: 10min

> An illegal character with code point 10 was found in this literal.

```sql
      165              ([^)\'\"]+)
      166              
      167              # fourth matching group
      168              # 1 or 0 quotation mark, 0 or more whitespace character(s)
>>>   169              ([\'\"]?\s*)
      170  
      171              # fifth matching group
      172              # a comma
      173              (,)
```

**Decisão**: 

### 15 · 🟠 CRITICAL · CODE_SMELL · `plsql:LiteralsNonPrintableCharactersCheck`
**Local**: `dbt_packages/codegen/macros/generate_model_import_ctes.sql:185` · **Effort**: 10min

> An illegal character with code point 10 was found in this literal.

```sql
      181              ([^)\'\"]+)
      182  
      183              # eighth matching group
      184              # 1 or 0 quotation mark, 0 or more whitespace character(s)            
>>>   185              ([\'\"]?\s*)
      186  
      187              # ninth matching group
      188              # a closing parenthesis, 0 or more whitespace character(s), closing }}            
      189              (\)\s*}})
```

**Decisão**: 

### 16 · 🟠 CRITICAL · CODE_SMELL · `plsql:S1192`
**Local**: `dbt_packages/codegen/macros/generate_model_import_ctes.sql:192` · **Effort**: 4min

> Define a constant instead of duplicating this literal 4 times.

```sql
      188              # a closing parenthesis, 0 or more whitespace character(s), closing }}            
      189              (\)\s*}})
      190              
      191              ',
>>>   192          'from_table_1':
      193              '(?ix)
      194              
      195              # first matching group
      196              # from or join followed by at least 1 whitespace character            
```

**Decisão**: 

### 17 · 🟠 CRITICAL · CODE_SMELL · `plsql:LiteralsNonPrintableCharactersCheck`
**Local**: `dbt_packages/codegen/macros/generate_model_import_ctes.sql:193` · **Effort**: 10min

> An illegal character with code point 10 was found in this literal.

```sql
      189              (\)\s*}})
      190              
      191              ',
      192          'from_table_1':
>>>   193              '(?ix)
      194              
      195              # first matching group
      196              # from or join followed by at least 1 whitespace character            
      197              (from|join)\s+
```

**Decisão**: 

### 18 · 🟠 CRITICAL · CODE_SMELL · `plsql:LiteralsNonPrintableCharactersCheck`
**Local**: `dbt_packages/codegen/macros/generate_model_import_ctes.sql:217` · **Effort**: 10min

> An illegal character with code point 10 was found in this literal.

```sql
      213              (\.)
      214              
      215              # sixth matching group
      216              # 1 or 0 of (opening bracket, backtick, or quotation mark)
>>>   217              ([\[`\"\']?)
      218              
      219              # seventh matching group
      220              # at least 1 word character
      221              (\w+)
```

**Decisão**: 

### 19 · 🟠 CRITICAL · CODE_SMELL · `plsql:LiteralsNonPrintableCharactersCheck`
**Local**: `dbt_packages/codegen/macros/generate_model_import_ctes.sql:227` · **Effort**: 10min

> An illegal character with code point 10 was found in this literal.

```sql
      223              # eighth matching group
      224              # 1 or 0 of (closing bracket, backtick, or quotation mark) folowed by a whitespace character or end of string
      225              ([\]`\"\']?)(?=\s|$)
      226              
>>>   227              ',
      228          'from_table_2':
      229              '(?ix)
      230  
      231              # first matching group
```

**Decisão**: 

### 20 · 🟠 CRITICAL · CODE_SMELL · `plsql:LiteralsNonPrintableCharactersCheck`
**Local**: `dbt_packages/codegen/macros/generate_model_import_ctes.sql:228` · **Effort**: 10min

> An illegal character with code point 10 was found in this literal.

```sql
      224              # 1 or 0 of (closing bracket, backtick, or quotation mark) folowed by a whitespace character or end of string
      225              ([\]`\"\']?)(?=\s|$)
      226              
      227              ',
>>>   228          'from_table_2':
      229              '(?ix)
      230  
      231              # first matching group
      232              # from or join followed by at least 1 whitespace character 
```

**Decisão**: 

### 21 · 🟠 CRITICAL · CODE_SMELL · `plsql:LiteralsNonPrintableCharactersCheck`
**Local**: `dbt_packages/codegen/macros/generate_model_import_ctes.sql:245` · **Effort**: 10min

> An illegal character with code point 10 was found in this literal.

```sql
      241              (\w+)
      242  
      243              # fouth matching group
      244              # 1 or 0 of (closing bracket, backtick, or quotation mark)            
>>>   245              ([\]`\"\']?)
      246              
      247              # fifth matching group
      248              # a period            
      249              (\.)
```

**Decisão**: 

### 22 · 🟠 CRITICAL · CODE_SMELL · `plsql:LiteralsNonPrintableCharactersCheck`
**Local**: `dbt_packages/codegen/macros/generate_model_import_ctes.sql:269` · **Effort**: 10min

> An illegal character with code point 10 was found in this literal.

```sql
      265              (\.)
      266              
      267              # tenth matching group
      268              # 1 or 0 of (closing bracket, backtick, or quotation mark)             
>>>   269              ([\[`\"\']?)
      270              
      271              # eleventh matching group
      272              # at least 1 word character   
      273              (\w+)
```

**Decisão**: 

### 23 · 🟠 CRITICAL · CODE_SMELL · `plsql:LiteralsNonPrintableCharactersCheck`
**Local**: `dbt_packages/codegen/macros/generate_model_import_ctes.sql:279` · **Effort**: 10min

> An illegal character with code point 10 was found in this literal.

```sql
      275              # twelfth matching group
      276              # 1 or 0 of (closing bracket, backtick, or quotation mark) folowed by a whitespace character or end of string
      277              ([\]`\"\']?)(?=\s|$)
      278              
>>>   279              ',
      280          'from_table_3':
      281              '(?ix)
      282  
      283              # first matching group
```

**Decisão**: 

### 24 · 🟠 CRITICAL · CODE_SMELL · `plsql:LiteralsNonPrintableCharactersCheck`
**Local**: `dbt_packages/codegen/macros/generate_model_import_ctes.sql:280` · **Effort**: 10min

> An illegal character with code point 10 was found in this literal.

```sql
      276              # 1 or 0 of (closing bracket, backtick, or quotation mark) folowed by a whitespace character or end of string
      277              ([\]`\"\']?)(?=\s|$)
      278              
      279              ',
>>>   280          'from_table_3':
      281              '(?ix)
      282  
      283              # first matching group
      284              # from or join followed by at least 1 whitespace character             
```

**Decisão**: 

### 25 · 🟠 CRITICAL · CODE_SMELL · `plsql:LiteralsNonPrintableCharactersCheck`
**Local**: `dbt_packages/codegen/macros/generate_model_import_ctes.sql:297` · **Effort**: 10min

> An illegal character with code point 10 was found in this literal.

```sql
      293              ([\w ]+)
      294  
      295              # fourth matching group
      296              # 1 or 0 of (closing bracket, backtick, or quotation mark) folowed by a whitespace character or end of string
>>>   297              ([\]`\"\'])(?=\s|$)
      298              
      299              ',
      300          'config_block':'(?i)(?s)^.*{{\s*config\s*\([^)]+\)\s*}}'
      301      } -%}
```

**Decisão**: 

### 26 · 🟠 CRITICAL · CODE_SMELL · `plsql:S1192`
**Local**: `dbt_packages/codegen/macros/generate_model_import_ctes.sql:300` · **Effort**: 4min

> Define a constant instead of duplicating this literal 3 times.

```sql
      296              # 1 or 0 of (closing bracket, backtick, or quotation mark) folowed by a whitespace character or end of string
      297              ([\]`\"\'])(?=\s|$)
      298              
      299              ',
>>>   300          'config_block':'(?i)(?s)^.*{{\s*config\s*\([^)]+\)\s*}}'
      301      } -%}
      302  
      303      {%- set from_list = [] -%}
      304      {%- set config_list = [] -%}
```

**Decisão**: 

### 27 · 🟠 CRITICAL · CODE_SMELL · `plsql:S1192`
**Local**: `dbt_packages/codegen/macros/generate_model_import_ctes.sql:326` · **Effort**: 4min

> Define a constant instead of duplicating this literal 3 times.

```sql
      322                  {%- set full_from_clause = match[1:]|join()|trim -%}
      323                  {%- set cte_name = match[2]|lower + '_' + match[6]|lower -%}
      324                  {%- set match_tuple = (cte_name, full_from_clause, regex_name) -%}
      325                  {%- do from_list.append(match_tuple) -%}   
>>>   326              {%- elif regex_name == 'from_table_2' -%}
      327                  {%- set full_from_clause = match[1:]|join()|trim -%}
      328                  {%- set cte_name = match[2]|lower + '_' + match[6]|lower + '_' + match[10]|lower -%}
      329                  {%- set match_tuple = (cte_name, full_from_clause, regex_name) -%}
      330                  {%- do from_list.append(match_tuple) -%}                     
```

**Decisão**: 

### 28 · 🟠 CRITICAL · CODE_SMELL · `plsql:LiteralsNonPrintableCharactersCheck`
**Local**: `dbt_packages/codegen/macros/helpers/helpers.sql:12` · **Effort**: 10min

> An illegal character with code point 10 was found in this literal.

```sql
        8  
        9  {# add to an input dictionary entries containing all the column descriptions of a given model #}
       10  {% macro add_model_column_descriptions_to_dict(resource_type, model_name, dict_with_descriptions={}) %}
       11      {% if resource_type == 'source' %}
>>>    12          {# sources aren't part of graph.nodes #}
       13          {% set nodes = graph.sources %}
       14      {% else %}
       15          {% set nodes = graph.nodes %}
       16      {% endif %}
```

**Decisão**: 

### 29 · 🟠 CRITICAL · CODE_SMELL · `plsql:LiteralsNonPrintableCharactersCheck`
**Local**: `dbt_packages/codegen/macros/helpers/helpers.sql:18` · **Effort**: 10min

> An illegal character with code point 10 was found in this literal.

```sql
       14      {% else %}
       15          {% set nodes = graph.nodes %}
       16      {% endif %}
       17      {% for node in nodes.values()
>>>    18          | selectattr('resource_type', 'equalto', resource_type)
       19          | selectattr('name', 'equalto', model_name) %}
       20          {% for col_name, col_values in node.columns.items() %}
       21              {% do dict_with_descriptions.update( {col_name: col_values.description} ) %}
       22          {% endfor %}
```

**Decisão**: 

### 30 · 🟠 CRITICAL · CODE_SMELL · `plsql:LiteralsNonPrintableCharactersCheck`
**Local**: `dbt_packages/codegen/macros/helpers/helpers.sql:19` · **Effort**: 10min

> An illegal character with code point 10 was found in this literal.

```sql
       15          {% set nodes = graph.nodes %}
       16      {% endif %}
       17      {% for node in nodes.values()
       18          | selectattr('resource_type', 'equalto', resource_type)
>>>    19          | selectattr('name', 'equalto', model_name) %}
       20          {% for col_name, col_values in node.columns.items() %}
       21              {% do dict_with_descriptions.update( {col_name: col_values.description} ) %}
       22          {% endfor %}
       23      {% endfor %}
```

**Decisão**: 

### 31 · 🟠 CRITICAL · CODE_SMELL · `plsql:LiteralsNonPrintableCharactersCheck`
**Local**: `dbt_packages/codegen/macros/helpers/helpers.sql:34` · **Effort**: 10min

> An illegal character with code point 10 was found in this literal.

```sql
       30      {% if execute %}
       31          {% set glob_dict = {} %}
       32          {% for full_model in codegen.get_model_dependencies(model_name) %}
       33              {% do codegen.add_model_column_descriptions_to_dict(
>>>    34                  full_model.split('.')[0], full_model.split('.')[-1], glob_dict
       35              ) %}
       36          {% endfor %}
       37          {{ return(glob_dict) }}
       38      {% endif %}
```

**Decisão**: 

### 32 · 🟠 CRITICAL · CODE_SMELL · `plsql:LiteralsNonPrintableCharactersCheck`
**Local**: `dbt_packages/codegen/macros/helpers/helpers.sql:45` · **Effort**: 10min

> An illegal character with code point 10 was found in this literal.

```sql
       41  {# build a list of models looping through all models in the project #}
       42  {# filter by directory or prefix arguments, if provided #}
       43  {% macro get_models(directory=None, prefix=None) %}
       44      {% set model_names=[] %}
>>>    45      {% set models = graph.nodes.values() | selectattr('resource_type', "equalto", 'model') %}
       46      {% if directory and prefix %}
       47          {% for model in models %}
       48              {% set model_path = "/".join(model.path.split("/")[:-1]) %}
       49              {% if model_path == directory and model.name.startswith(prefix) %}
```

**Decisão**: 

### 33 · 🟠 CRITICAL · CODE_SMELL · `plsql:LiteralsNonPrintableCharactersCheck`
**Local**: `dbt_packages/codegen/macros/helpers/helpers.sql:73` · **Effort**: 10min

> An illegal character with code point 10 was found in this literal.

```sql
       69      {{ return(model_names) }}
       70  {% endmacro %}
       71  
       72  {% macro data_type_format_source(column) -%}
>>>    73    {{ return(adapter.dispatch('data_type_format_source', 'codegen')(column)) }}
       74  {%- endmacro %}
       75  
       76  {# format a column data type for a source #}
       77  {% macro default__data_type_format_source(column) %}
```

**Decisão**: 

### 34 · 🟠 CRITICAL · CODE_SMELL · `plsql:LiteralsNonPrintableCharactersCheck`
**Local**: `dbt_packages/codegen/macros/helpers/helpers.sql:79` · **Effort**: 10min

> An illegal character with code point 10 was found in this literal.

```sql
       75  
       76  {# format a column data type for a source #}
       77  {% macro default__data_type_format_source(column) %}
       78      {% set formatted = codegen.format_column(column) %}
>>>    79      {{ return(formatted['data_type'] | lower) }}
       80  {% endmacro %}
       81  
       82  {% macro data_type_format_model(column) -%}
       83    {{ return(adapter.dispatch('data_type_format_model', 'codegen')(column)) }}
```

**Decisão**: 

### 35 · 🟠 CRITICAL · CODE_SMELL · `plsql:LiteralsNonPrintableCharactersCheck`
**Local**: `dbt_packages/codegen/macros/helpers/helpers.sql:83` · **Effort**: 10min

> An illegal character with code point 10 was found in this literal.

```sql
       79      {{ return(formatted['data_type'] | lower) }}
       80  {% endmacro %}
       81  
       82  {% macro data_type_format_model(column) -%}
>>>    83    {{ return(adapter.dispatch('data_type_format_model', 'codegen')(column)) }}
       84  {%- endmacro %}
       85  
       86  {# format a column data type for a model #}
       87  {% macro default__data_type_format_model(column) %}
```

**Decisão**: 

### 36 · 🟠 CRITICAL · CODE_SMELL · `plsql:S1192`
**Local**: `dbt_packages/dbt_utils/integration_tests/models/sql/test_get_column_values.sql:2` · **Effort**: 4min

> Define a constant instead of duplicating this literal 3 times.

```sql
        1  
>>>     2  {% set column_values = dbt_utils.get_column_values(ref('data_get_column_values'), 'field', default=[], order_by="field") %}
        3  
        4  
        5  {% if target.type == 'snowflake' %}
        6  
```

**Decisão**: 

### 37 · 🟠 CRITICAL · CODE_SMELL · `plsql:S1192`
**Local**: `dbt_packages/dbt_utils/integration_tests/models/sql/test_get_single_value.sql:8` · **Effort**: 4min

> Define a constant instead of duplicating this literal 5 times.

```sql
        4      I once thought as you are thinking. Proceed with caution.
        5  #}
        6  
        7  {% set date_statement %}
>>>     8      select date_value from {{ ref('data_get_single_value') }}
        9  {% endset %}
       10  
       11  {% set float_statement %}
       12      select float_value from {{ ref('data_get_single_value') }}
```

**Decisão**: 

### 38 · 🟠 CRITICAL · CODE_SMELL · `plsql:LiteralsNonPrintableCharactersCheck`
**Local**: `dbt_packages/dbt_utils/integration_tests/tests/assert_get_query_results_as_dict_objects_equal.sql:23` · **Effort**: 10min

> An illegal character with code point 10 was found in this literal.

```sql
       19  {% set actual_dictionary=dbt_utils.get_query_results_as_dict(
       20      "select * from " ~ ref('data_get_query_results_as_dict') ~ " order by 1"
       21  ) %}
       22  {#-
>>>    23  For reasons that remain unclear, Jinja won't return True for actual_dictionary == expected_dictionary.
       24  Instead, we'll manually check that the values of these dictionaries are equivalent.
       25  -#}
       26  
       27  {% set ns = namespace(
```

**Decisão**: 

### 39 · 🟠 CRITICAL · CODE_SMELL · `plsql:LiteralsNonPrintableCharactersCheck`
**Local**: `dbt_packages/dbt_utils/integration_tests/tests/generic/expect_table_columns_to_match_set.sql:3` · **Effort**: 10min

> An illegal character with code point 10 was found in this literal.

```sql
        1  {#
        2      This macro is copied and slightly edited from the dbt_expectations package.
>>>     3      At the time of this addition, dbt_expectations couldn't be added because
        4      integration_tests is installing dbt_utils from local without a hard-coded
        5      path. dbt is not able to resolve duplicate dependencies of dbt_utils
        6      due to this.
        7  #}
```

**Decisão**: 

### 40 · 🟠 CRITICAL · CODE_SMELL · `plsql:LiteralsNonPrintableCharactersCheck`
**Local**: `dbt_packages/dbt_utils/integration_tests/tests/generic/expect_table_columns_to_match_set.sql:31` · **Effort**: 10min

> An illegal character with code point 10 was found in this literal.

```sql
       27  
       28      with relation_columns as (
       29  
       30          {% for col_name in relation_column_names %}
>>>    31          select cast('{{ col_name }}' as {{ type_string() }}) as relation_column
       32          {% if not loop.last %}union all{% endif %}
       33          {% endfor %}
       34      ),
       35      input_columns as (
```

**Decisão**: 

### 41 · 🟠 CRITICAL · CODE_SMELL · `plsql:S1192`
**Local**: `dbt_packages/dbt_utils/macros/generic_tests/equality.sql:2` · **Effort**: 4min

> Define a constant instead of duplicating this literal 6 times.

```sql
        1  {% test equality(model, compare_model, compare_columns=None, exclude_columns=None, precision = None) %}
>>>     2    {{ return(adapter.dispatch('test_equality', 'dbt_utils')(model, compare_model, compare_columns, exclude_columns, precision)) }}
        3  {% endtest %}
        4  
        5  {% macro default__test_equality(model, compare_model, compare_columns=None, exclude_columns=None, precision = None) %}
        6  
```

**Decisão**: 

### 42 · 🟠 CRITICAL · CODE_SMELL · `plsql:S1192`
**Local**: `dbt_packages/dbt_utils/macros/generic_tests/equality.sql:58` · **Effort**: 4min

> Define a constant instead of duplicating this literal 6 times.

```sql
       54                  {% do include_model_columns.append(column) %}
       55              {%- endif %}
       56          {%- endfor %}
       57  
>>>    58          {%- set compare_columns_set = set(include_columns | map(attribute='quoted') | map("lower")) %}
       59          {%- set compare_model_columns_set = set(include_model_columns | map(attribute='quoted') | map("lower")) %}
       60      {%- else -%}
       61          {%- set compare_columns_set = set(model_columns | map(attribute='quoted') | map("lower")) %}
       62          {%- set compare_model_columns_set = set(compare_model_columns | map(attribute='quoted') | map("lower")) %}
```

**Decisão**: 

### 43 · 🟠 CRITICAL · CODE_SMELL · `plsql:S1192`
**Local**: `dbt_packages/dbt_utils/macros/generic_tests/mutually_exclusive_ranges.sql:1` · **Effort**: 4min

> Define a constant instead of duplicating this literal 3 times.

```sql
>>>     1  {% test mutually_exclusive_ranges(model, lower_bound_column, upper_bound_column, partition_by=None, gaps='allowed', zero_length_range_allowed=False) %}
        2    {{ return(adapter.dispatch('test_mutually_exclusive_ranges', 'dbt_utils')(model, lower_bound_column, upper_bound_column, partition_by, gaps, zero_length_range_allowed)) }}
        3  {% endtest %}
        4  
        5  {% macro default__test_mutually_exclusive_ranges(model, lower_bound_column, upper_bound_column, partition_by=None, gaps='allowed', zero_length_range_allowed=False) %}
```

**Decisão**: 

### 44 · 🟠 CRITICAL · CODE_SMELL · `plsql:S1192`
**Local**: `dbt_packages/dbt_utils/macros/sql/date_spine.sql:2` · **Effort**: 4min

> Define a constant instead of duplicating this literal 3 times.

```sql
        1  {% macro get_intervals_between(start_date, end_date, datepart) -%}
>>>     2      {{ return(adapter.dispatch('get_intervals_between', 'dbt_utils')(start_date, end_date, datepart)) }}
        3  {%- endmacro %}
        4  
        5  {% macro default__get_intervals_between(start_date, end_date, datepart) -%}
        6      {%- call statement('get_intervals_between', fetch_result=True) %}
```

**Decisão**: 

### 45 · 🟠 CRITICAL · CODE_SMELL · `plsql:S1192`
**Local**: `dbt_packages/dbt_utils/macros/sql/get_column_values.sql:2` · **Effort**: 4min

> Define a constant instead of duplicating this literal 4 times.

```sql
        1  {% macro get_column_values(table, column, order_by='count(*) desc', max_records=none, default=none, where=none) -%}
>>>     2      {{ return(adapter.dispatch('get_column_values', 'dbt_utils')(table, column, order_by, max_records, default, where)) }}
        3  {% endmacro %}
        4  
        5  {% macro default__get_column_values(table, column, order_by='count(*) desc', max_records=none, default=none, where=none) -%}
        6      {#-- Prevent querying of db in parsing mode. This works because this macro does not create any new refs. #}
```

**Decisão**: 

### 46 · 🟠 CRITICAL · CODE_SMELL · `plsql:S1192`
**Local**: `dbt_packages/dbt_utils/macros/sql/get_filtered_columns_in_relation.sql:2` · **Effort**: 4min

> Define a constant instead of duplicating this literal 3 times.

```sql
        1  {% macro get_filtered_columns_in_relation(from, except=[]) -%}
>>>     2      {{ return(adapter.dispatch('get_filtered_columns_in_relation', 'dbt_utils')(from, except)) }}
        3  {% endmacro %}
        4  
        5  {% macro default__get_filtered_columns_in_relation(from, except=[]) -%}
        6      {%- do dbt_utils._is_relation(from, 'get_filtered_columns_in_relation') -%}
```

**Decisão**: 

### 47 · 🟠 CRITICAL · CODE_SMELL · `plsql:S1192`
**Local**: `dbt_packages/dbt_utils/macros/sql/get_table_types_sql.sql:7` · **Effort**: 4min

> Define a constant instead of duplicating this literal 4 times.

```sql
        3  {%- endmacro -%}
        4  
        5  {% macro default__get_table_types_sql() %}
        6              case table_type
>>>     7                  when 'BASE TABLE' then 'table'
        8                  when 'EXTERNAL TABLE' then 'external'
        9                  when 'MATERIALIZED VIEW' then 'materializedview'
       10                  else lower(table_type)
       11              end as {{ adapter.quote('table_type') }}
```

**Decisão**: 

### 48 · 🟠 CRITICAL · CODE_SMELL · `plsql:S1192`
**Local**: `dbt_packages/dbt_utils/macros/sql/get_table_types_sql.sql:7` · **Effort**: 4min

> Define a constant instead of duplicating this literal 3 times.

```sql
        3  {%- endmacro -%}
        4  
        5  {% macro default__get_table_types_sql() %}
        6              case table_type
>>>     7                  when 'BASE TABLE' then 'table'
        8                  when 'EXTERNAL TABLE' then 'external'
        9                  when 'MATERIALIZED VIEW' then 'materializedview'
       10                  else lower(table_type)
       11              end as {{ adapter.quote('table_type') }}
```

**Decisão**: 

### 49 · 🟠 CRITICAL · CODE_SMELL · `plsql:S1192`
**Local**: `dbt_packages/dbt_utils/macros/sql/get_table_types_sql.sql:9` · **Effort**: 4min

> Define a constant instead of duplicating this literal 3 times.

```sql
        5  {% macro default__get_table_types_sql() %}
        6              case table_type
        7                  when 'BASE TABLE' then 'table'
        8                  when 'EXTERNAL TABLE' then 'external'
>>>     9                  when 'MATERIALIZED VIEW' then 'materializedview'
       10                  else lower(table_type)
       11              end as {{ adapter.quote('table_type') }}
       12  {% endmacro %}
       13  
```

**Decisão**: 

### 50 · 🟠 CRITICAL · CODE_SMELL · `plsql:S1192`
**Local**: `dbt_packages/dbt_utils/macros/sql/get_table_types_sql.sql:9` · **Effort**: 4min

> Define a constant instead of duplicating this literal 3 times.

```sql
        5  {% macro default__get_table_types_sql() %}
        6              case table_type
        7                  when 'BASE TABLE' then 'table'
        8                  when 'EXTERNAL TABLE' then 'external'
>>>     9                  when 'MATERIALIZED VIEW' then 'materializedview'
       10                  else lower(table_type)
       11              end as {{ adapter.quote('table_type') }}
       12  {% endmacro %}
       13  
```

**Decisão**: 

### 51 · 🟠 CRITICAL · CODE_SMELL · `plsql:S1192`
**Local**: `dbt_packages/dbt_utils/macros/sql/get_table_types_sql.sql:11` · **Effort**: 4min

> Define a constant instead of duplicating this literal 3 times.

```sql
        7                  when 'BASE TABLE' then 'table'
        8                  when 'EXTERNAL TABLE' then 'external'
        9                  when 'MATERIALIZED VIEW' then 'materializedview'
       10                  else lower(table_type)
>>>    11              end as {{ adapter.quote('table_type') }}
       12  {% endmacro %}
       13  
       14  
       15  {% macro postgres__get_table_types_sql() %}
```

**Decisão**: 

### 52 · 🟠 CRITICAL · CODE_SMELL · `plsql:S1192`
**Local**: `dbt_packages/dbt_utils/macros/sql/get_tables_by_pattern_sql.sql:9` · **Effort**: 4min

> Define a constant instead of duplicating this literal 3 times.

```sql
        5  
        6  {% macro default__get_tables_by_pattern_sql(schema_pattern, table_pattern, exclude='', database=target.database) %}
        7  
        8          select distinct
>>>     9              table_schema as {{ adapter.quote('table_schema') }},
       10              table_name as {{ adapter.quote('table_name') }},
       11              {{ dbt_utils.get_table_types_sql() }}
       12          from {{ database }}.information_schema.tables
       13          where table_schema ilike '{{ schema_pattern }}'
```

**Decisão**: 

### 53 · 🟠 CRITICAL · CODE_SMELL · `plsql:S1192`
**Local**: `dbt_packages/dbt_utils/macros/sql/get_tables_by_pattern_sql.sql:10` · **Effort**: 4min

> Define a constant instead of duplicating this literal 3 times.

```sql
        6  {% macro default__get_tables_by_pattern_sql(schema_pattern, table_pattern, exclude='', database=target.database) %}
        7  
        8          select distinct
        9              table_schema as {{ adapter.quote('table_schema') }},
>>>    10              table_name as {{ adapter.quote('table_name') }},
       11              {{ dbt_utils.get_table_types_sql() }}
       12          from {{ database }}.information_schema.tables
       13          where table_schema ilike '{{ schema_pattern }}'
       14          and table_name ilike '{{ table_pattern }}'
```

**Decisão**: 

### 54 · 🟠 CRITICAL · CODE_SMELL · `plsql:S1192`
**Local**: `dbt_packages/dbt_utils/macros/sql/get_tables_by_pattern_sql.sql:13` · **Effort**: 4min

> Define a constant instead of duplicating this literal 4 times.

```sql
        9              table_schema as {{ adapter.quote('table_schema') }},
       10              table_name as {{ adapter.quote('table_name') }},
       11              {{ dbt_utils.get_table_types_sql() }}
       12          from {{ database }}.information_schema.tables
>>>    13          where table_schema ilike '{{ schema_pattern }}'
       14          and table_name ilike '{{ table_pattern }}'
       15          and table_name not ilike '{{ exclude }}'
       16  
       17  {% endmacro %}
```

**Decisão**: 

### 55 · 🟠 CRITICAL · CODE_SMELL · `plsql:S1192`
**Local**: `dbt_packages/dbt_utils/macros/sql/get_tables_by_pattern_sql.sql:14` · **Effort**: 4min

> Define a constant instead of duplicating this literal 4 times.

```sql
       10              table_name as {{ adapter.quote('table_name') }},
       11              {{ dbt_utils.get_table_types_sql() }}
       12          from {{ database }}.information_schema.tables
       13          where table_schema ilike '{{ schema_pattern }}'
>>>    14          and table_name ilike '{{ table_pattern }}'
       15          and table_name not ilike '{{ exclude }}'
       16  
       17  {% endmacro %}
       18  
```

**Decisão**: 

### 56 · 🟠 CRITICAL · CODE_SMELL · `plsql:S1192`
**Local**: `dbt_packages/dbt_utils/macros/sql/get_tables_by_pattern_sql.sql:15` · **Effort**: 4min

> Define a constant instead of duplicating this literal 4 times.

```sql
       11              {{ dbt_utils.get_table_types_sql() }}
       12          from {{ database }}.information_schema.tables
       13          where table_schema ilike '{{ schema_pattern }}'
       14          and table_name ilike '{{ table_pattern }}'
>>>    15          and table_name not ilike '{{ exclude }}'
       16  
       17  {% endmacro %}
       18  
       19  {% macro redshift__get_tables_by_pattern_sql(schema_pattern, table_pattern, exclude='', database=target.database) %}
```

**Decisão**: 

### 57 · 🟠 CRITICAL · CODE_SMELL · `plsql:S1192`
**Local**: `dbt_packages/dbt_utils/macros/sql/nullcheck_table.sql:2` · **Effort**: 4min

> Define a constant instead of duplicating this literal 3 times.

```sql
        1  {% macro nullcheck_table(relation) %}
>>>     2      {{ return(adapter.dispatch('nullcheck_table', 'dbt_utils')(relation)) }}
        3  {% endmacro %}
        4  
        5  {% macro default__nullcheck_table(relation) %}
        6  
```

**Decisão**: 

### 58 · 🟠 CRITICAL · CODE_SMELL · `plsql:LiteralsNonPrintableCharactersCheck`
**Local**: `dbt_packages/dbt_utils/macros/sql/safe_add.sql:9` · **Effort**: 10min

> An illegal character with code point 10 was found in this literal.

```sql
        5  {%- macro default__safe_add(field_list) -%}
        6  
        7  {%- if field_list is not iterable or field_list is string or field_list is mapping -%}
        8  
>>>     9  {%- set error_message = '
       10  Warning: the `safe_add` macro now takes a single list argument instead of \
       11  string arguments. The {}.{} model triggered this warning. \
       12  '.format(model.package_name, model.name) -%}
       13  
```

**Decisão**: 

### 59 · 🟠 CRITICAL · CODE_SMELL · `plsql:LiteralsNonPrintableCharactersCheck`
**Local**: `dbt_packages/dbt_utils/macros/sql/safe_subtract.sql:9` · **Effort**: 10min

> An illegal character with code point 10 was found in this literal.

```sql
        5  {%- macro default__safe_subtract(field_list) -%}
        6  
        7  {%- if field_list is not iterable or field_list is string or field_list is mapping -%}
        8  
>>>     9  {%- set error_message = '
       10  Warning: the `safe_subtract` macro takes a single list argument instead of \
       11  string arguments. The {}.{} model triggered this warning. \
       12  '.format(model.package_name, model.name) -%}
       13  
```

**Decisão**: 

### 60 · 🟠 CRITICAL · CODE_SMELL · `plsql:LiteralsNonPrintableCharactersCheck`
**Local**: `dbt_packages/dbt_utils/macros/sql/surrogate_key.sql:8` · **Effort**: 10min

> An illegal character with code point 10 was found in this literal.

```sql
        4  {% endmacro %}
        5  
        6  {%- macro default__surrogate_key(field_list) -%}
        7  
>>>     8  {%- set error_message = '
        9  Warning: `dbt_utils.surrogate_key` has been replaced by \
       10  `dbt_utils.generate_surrogate_key`. The new macro treats null values \
       11  differently to empty strings. To restore the behaviour of the original \
       12  macro, add a global variable in dbt_project.yml called \
```

**Decisão**: 

### 61 · 🟠 CRITICAL · CODE_SMELL · `plsql:S1192`
**Local**: `dbt_packages/dbt_utils/macros/sql/union.sql:2` · **Effort**: 4min

> Define a constant instead of duplicating this literal 3 times.

```sql
        1  {%- macro union_relations(relations, column_override=none, include=[], exclude=[], source_column_name='_dbt_source_relation', where=none) -%}
>>>     2      {{ return(adapter.dispatch('union_relations', 'dbt_utils')(relations, column_override, include, exclude, source_column_name, where)) }}
        3  {% endmacro %}
        4  
        5  {%- macro default__union_relations(relations, column_override=none, include=[], exclude=[], source_column_name='_dbt_source_relation', where=none) -%}
        6  
```

**Decisão**: 

### 62 · 🟠 CRITICAL · CODE_SMELL · `plsql:S1192`
**Local**: `dbt_packages/dbt_utils/macros/sql/unpivot.sql:16` · **Effort**: 4min

> Define a constant instead of duplicating this literal 3 times.

```sql
       12      value_name: Destination table column name for the pivoted values
       13  #}
       14  
       15  {% macro unpivot(relation=none, cast_to='varchar', exclude=none, remove=none, field_name='field_name', value_name='value', quote_identifiers=False) -%}
>>>    16      {{ return(adapter.dispatch('unpivot', 'dbt_utils')(relation, cast_to, exclude, remove, field_name, value_name, quote_identifiers)) }}
       17  {% endmacro %}
       18  
       19  {% macro default__unpivot(relation=none, cast_to='varchar', exclude=none, remove=none, field_name='field_name', value_name='value', quote_identifiers=False) -%}
       20  
```

**Decisão**: 

### 63 · 🟠 CRITICAL · CODE_SMELL · `python:S1192`
**Local**: `src/flext_dbt_ldif/models.py:52` · **Effort**: 8min

> Define a constant instead of duplicating this literal "Validation lifecycle status." 4 times.

```python
       48              """Validated LDIF quality metrics."""
       49  
       50              total_entries: int = u.Field(description="Total LDIF entries validated.")
       51              quality_score: float = u.Field(description="Aggregate LDIF quality score.")
>>>    52              validation_status: str = u.Field(description="Validation lifecycle status.")
       53  
       54          class DbtTransformationResult(m.ArbitraryTypesModel):
       55              """DBT transformation execution summary."""
       56  
```

**Decisão**: 

### 64 · 🟠 CRITICAL · CODE_SMELL · `python:S1192`
**Local**: `src/flext_dbt_ldif/models.py:62` · **Effort**: 6min

> Define a constant instead of duplicating this literal "Transformation lifecycle status." 3 times.

```python
       58              models: t.StrSequence = u.Field(
       59                  default_factory=tuple,
       60                  description="Names of models produced by the transformation",
       61              )
>>>    62              status: str = u.Field(description="Transformation lifecycle status.")
       63  
       64          class ModelGenerationResult(m.ArbitraryTypesModel):
       65              """Generated model metadata summary."""
       66  
```

**Decisão**: 

### 65 · 🟡 MAJOR · CODE_SMELL · `shelldre:S7688`
**Local**: `.github/scripts/install-git-hooks.sh:55` · **Effort**: 2min

> Use '[[' instead of '[' for conditional tests. The '[[' construct is safer and more feature-rich.

```bash
       51  _log "Installing Beads git hooks (chained) at ${WORKSPACE_ROOT}"
       52  bd hooks install --chain >/dev/null || fail "bd hooks install --chain failed"
       53  
       54  hook_path="$(git rev-parse --git-path hooks/prepare-commit-msg)"
>>>    55  [ -f "${hook_path}" ] || fail "prepare-commit-msg hook missing after bd hooks install"
       56  
       57  _log "Applying FLEXT agent-trailer guard to ${hook_path}"
       58  GUARD_TOKEN="BD_ALLOW_AGENT_COMMIT_TRAILERS" python3 - "${hook_path}" <<'PY'
       59  import os
```

**Decisão**: 

### 66 · 🟡 MAJOR · CODE_SMELL · `shelldre:S7688`
**Local**: `.github/scripts/install-git-hooks.sh:104` · **Effort**: 2min

> Use '[[' instead of '[' for conditional tests. The '[[' construct is safer and more feature-rich.

```bash
      100  grep -q 'BD_ALLOW_AGENT_COMMIT_TRAILERS' "${hook_path}" \
      101  	|| fail "guard token missing after injection"
      102  grep -q 'bd hooks run prepare-commit-msg' "${hook_path}" \
      103  	|| fail "bd delegation missing; refusing to leave hook without beads integration"
>>>   104  [ -f "$(git rev-parse --git-path hooks/pre-commit)" ] \
      105  	|| fail "pre-commit hook missing after provisioning"
      106  [ -f "$(git rev-parse --git-path hooks/pre-push)" ] \
      107  	|| fail "pre-push hook missing after provisioning"
      108  
```

**Decisão**: 

### 67 · 🟡 MAJOR · CODE_SMELL · `shelldre:S7688`
**Local**: `.github/scripts/install-git-hooks.sh:106` · **Effort**: 2min

> Use '[[' instead of '[' for conditional tests. The '[[' construct is safer and more feature-rich.

```bash
      102  grep -q 'bd hooks run prepare-commit-msg' "${hook_path}" \
      103  	|| fail "bd delegation missing; refusing to leave hook without beads integration"
      104  [ -f "$(git rev-parse --git-path hooks/pre-commit)" ] \
      105  	|| fail "pre-commit hook missing after provisioning"
>>>   106  [ -f "$(git rev-parse --git-path hooks/pre-push)" ] \
      107  	|| fail "pre-push hook missing after provisioning"
      108  
      109  echo "install-git-hooks: prepare-commit-msg guarded (BD_ALLOW_AGENT_COMMIT_TRAILERS opt-in)"
```

**Decisão**: 

### 68 · 🟡 MAJOR · VULNERABILITY · `githubactions:S8264`
**Local**: `.github/workflows/docs.yml:18` · **Effort**: 5min

> Move this read permission from workflow level to job level.

```yaml
       14        - ".github/workflows/docs.yml"
       15    workflow_dispatch:
       16  
       17  permissions:
>>>    18    contents: read
       19    pages: write
       20    id-token: write
       21  
       22  concurrency:
```

**Decisão**: 

### 69 · 🟡 MAJOR · VULNERABILITY · `githubactions:S8233`
**Local**: `.github/workflows/docs.yml:19` · **Effort**: 5min

> Move this write permission from workflow level to job level.

```yaml
       15    workflow_dispatch:
       16  
       17  permissions:
       18    contents: read
>>>    19    pages: write
       20    id-token: write
       21  
       22  concurrency:
       23    group: pages
```

**Decisão**: 

### 70 · 🟡 MAJOR · VULNERABILITY · `githubactions:S8233`
**Local**: `.github/workflows/docs.yml:20` · **Effort**: 5min

> Move this write permission from workflow level to job level.

```yaml
       16  
       17  permissions:
       18    contents: read
       19    pages: write
>>>    20    id-token: write
       21  
       22  concurrency:
       23    group: pages
       24    cancel-in-progress: false
```

**Decisão**: 

### 71 · 🟡 MAJOR · VULNERABILITY · `githubactions:S7637`
**Local**: `dbt_packages/codegen/.github/workflows/ci.yml:21` · **Effort**: 30min

> Use full commit SHA hash for this dependency.

```yaml
       17      workflow_dispatch:
       18  
       19  jobs:
       20    run-tests:
>>>    21        uses: dbt-labs/dbt-package-testing/.github/workflows/run_tox.yml@v1
       22        # this just tests with postgres so no variables need to be passed through.
       23        # When it's time to add more adapters you will need to pass through inputs for
       24        # the other adapters as shown in the below example for redshift
       25        with:
```

**Decisão**: 

### 72 · 🟡 MAJOR · VULNERABILITY · `githubactions:S7637`
**Local**: `dbt_packages/codegen/.github/workflows/stale.yml:30` · **Effort**: 30min

> Use full commit SHA hash for this dependency.

```yaml
       26    pull-requests: write
       27  
       28  jobs:
       29    stale:
>>>    30      uses: dbt-labs/actions/.github/workflows/stale-bot-matrix.yml@main
```

**Decisão**: 

### 73 · 🟡 MAJOR · VULNERABILITY · `githubactions:S7637`
**Local**: `dbt_packages/codegen/.github/workflows/triage-labels.yml:27` · **Effort**: 30min

> Use full commit SHA hash for this dependency.

```yaml
       23  
       24  jobs:
       25    triage_label:
       26      if: contains(github.event.issue.labels.*.name, 'awaiting_response')
>>>    27      uses: dbt-labs/actions/.github/workflows/swap-labels.yml@main
       28      with:
       29        add_label: "triage"
       30        remove_label: "awaiting_response"
       31      secrets: inherit
```

**Decisão**: 

### 74 · 🟡 MAJOR · VULNERABILITY · `githubactions:S7635`
**Local**: `dbt_packages/codegen/.github/workflows/triage-labels.yml:31` · **Effort**: 10min

> Only pass required secrets to this workflow.

```yaml
       27      uses: dbt-labs/actions/.github/workflows/swap-labels.yml@main
       28      with:
       29        add_label: "triage"
       30        remove_label: "awaiting_response"
>>>    31      secrets: inherit
```

**Decisão**: 

### 75 · 🟡 MAJOR · VULNERABILITY · `githubactions:S8544`
**Local**: `dbt_packages/dbt_utils/.github/workflows/ci.yml:43` · **Effort**: 1h

> Using dependencies without locking resolved versions is security-sensitive.

```yaml
       39                    python-version: ${{ env.PYTHON_VERSION }}
       40  
       41              - name: "Install tox"
       42                run: |
>>>    43                    python -m pip install --upgrade pip
       44                    pip install tox
       45  
       46              - name: "Get list of supported adapters or use input adapter only"
       47                id: list-adapters
```

**Decisão**: 

### 76 · 🟡 MAJOR · VULNERABILITY · `githubactions:S8541`
**Local**: `dbt_packages/dbt_utils/.github/workflows/ci.yml:44` · **Effort**: 1h

> Omitting "--only-binary :all:" can lead to the execution of setup scripts. Make sure it is safe here.

```yaml
       40  
       41              - name: "Install tox"
       42                run: |
       43                    python -m pip install --upgrade pip
>>>    44                    pip install tox
       45  
       46              - name: "Get list of supported adapters or use input adapter only"
       47                id: list-adapters
       48                run: |
```

**Decisão**: 

### 77 · 🟡 MAJOR · VULNERABILITY · `githubactions:S8544`
**Local**: `dbt_packages/dbt_utils/.github/workflows/ci.yml:44` · **Effort**: 1h

> Using dependencies without locking resolved versions is security-sensitive.

```yaml
       40  
       41              - name: "Install tox"
       42                run: |
       43                    python -m pip install --upgrade pip
>>>    44                    pip install tox
       45  
       46              - name: "Get list of supported adapters or use input adapter only"
       47                id: list-adapters
       48                run: |
```

**Decisão**: 

### 78 · 🟡 MAJOR · VULNERABILITY · `githubactions:S8544`
**Local**: `dbt_packages/dbt_utils/.github/workflows/ci.yml:106` · **Effort**: 1h

> Using dependencies without locking resolved versions is security-sensitive.

```yaml
      102                    python-version: ${{ env.PYTHON_VERSION }}
      103  
      104              - name: "Install ${{ matrix.adapter }}"
      105                run: |
>>>   106                    python -m pip install --upgrade pip
      107                    pip install dbt-${{ matrix.adapter }}
      108  
      109              - name: "Install tox"
      110                run: |
```

**Decisão**: 

### 79 · 🟡 MAJOR · VULNERABILITY · `githubactions:S8544`
**Local**: `dbt_packages/dbt_utils/.github/workflows/ci.yml:107` · **Effort**: 1h

> Using dependencies without locking resolved versions is security-sensitive.

```yaml
      103  
      104              - name: "Install ${{ matrix.adapter }}"
      105                run: |
      106                    python -m pip install --upgrade pip
>>>   107                    pip install dbt-${{ matrix.adapter }}
      108  
      109              - name: "Install tox"
      110                run: |
      111                    python -m pip install --upgrade pip
```

**Decisão**: 

### 80 · 🟡 MAJOR · VULNERABILITY · `githubactions:S8544`
**Local**: `dbt_packages/dbt_utils/.github/workflows/ci.yml:111` · **Effort**: 1h

> Using dependencies without locking resolved versions is security-sensitive.

```yaml
      107                    pip install dbt-${{ matrix.adapter }}
      108  
      109              - name: "Install tox"
      110                run: |
>>>   111                    python -m pip install --upgrade pip
      112                    pip install tox
      113  
      114              - name: "Run integration tests with tox on ${{ matrix.adapter }}"
      115                run: |
```

**Decisão**: 

### 81 · 🟡 MAJOR · VULNERABILITY · `githubactions:S8541`
**Local**: `dbt_packages/dbt_utils/.github/workflows/ci.yml:112` · **Effort**: 1h

> Omitting "--only-binary :all:" can lead to the execution of setup scripts. Make sure it is safe here.

```yaml
      108  
      109              - name: "Install tox"
      110                run: |
      111                    python -m pip install --upgrade pip
>>>   112                    pip install tox
      113  
      114              - name: "Run integration tests with tox on ${{ matrix.adapter }}"
      115                run: |
      116                    tox -e dbt_integration_${{ matrix.adapter }}
```

**Decisão**: 

### 82 · 🟡 MAJOR · VULNERABILITY · `githubactions:S8544`
**Local**: `dbt_packages/dbt_utils/.github/workflows/ci.yml:112` · **Effort**: 1h

> Using dependencies without locking resolved versions is security-sensitive.

```yaml
      108  
      109              - name: "Install tox"
      110                run: |
      111                    python -m pip install --upgrade pip
>>>   112                    pip install tox
      113  
      114              - name: "Run integration tests with tox on ${{ matrix.adapter }}"
      115                run: |
      116                    tox -e dbt_integration_${{ matrix.adapter }}
```

**Decisão**: 

### 83 · 🟡 MAJOR · VULNERABILITY · `githubactions:S7637`
**Local**: `dbt_packages/dbt_utils/.github/workflows/create-table-of-contents.yml:28` · **Effort**: 30min

> Use full commit SHA hash for this dependency.

```yaml
       24            curl https://raw.githubusercontent.com/ekalinin/github-markdown-toc/master/gh-md-toc -o gh-md-toc
       25            chmod a+x gh-md-toc
       26            ./gh-md-toc --insert --no-backup README.md
       27            rm ./gh-md-toc
>>>    28        - uses: stefanzweifel/git-auto-commit-action@v4
       29          with:
       30            commit_message: Auto update table of contents
```

**Decisão**: 

### 84 · 🟡 MAJOR · VULNERABILITY · `githubactions:S7637`
**Local**: `dbt_packages/dbt_utils/.github/workflows/stale.yml:30` · **Effort**: 30min

> Use full commit SHA hash for this dependency.

```yaml
       26    pull-requests: write
       27  
       28  jobs:
       29    stale:
>>>    30      uses: dbt-labs/actions/.github/workflows/stale-bot-matrix.yml@main
```

**Decisão**: 

### 85 · 🟡 MAJOR · VULNERABILITY · `githubactions:S7637`
**Local**: `dbt_packages/dbt_utils/.github/workflows/triage-labels.yml:27` · **Effort**: 30min

> Use full commit SHA hash for this dependency.

```yaml
       23  
       24  jobs:
       25    triage_label:
       26      if: contains(github.event.issue.labels.*.name, 'awaiting_response')
>>>    27      uses: dbt-labs/actions/.github/workflows/swap-labels.yml@main
       28      with:
       29        add_label: "triage"
       30        remove_label: "awaiting_response"
       31      secrets: inherit
```

**Decisão**: 

### 86 · 🟡 MAJOR · VULNERABILITY · `githubactions:S7635`
**Local**: `dbt_packages/dbt_utils/.github/workflows/triage-labels.yml:31` · **Effort**: 10min

> Only pass required secrets to this workflow.

```yaml
       27      uses: dbt-labs/actions/.github/workflows/swap-labels.yml@main
       28      with:
       29        add_label: "triage"
       30        remove_label: "awaiting_response"
>>>    31      secrets: inherit
```

**Decisão**: 

### 87 · 🟡 MAJOR · VULNERABILITY · `text:S8565`
**Local**: `pyproject.toml:-` · **Effort**: 5min

> Dependency versions are not predictable if the lock file (uv.lock, poetry.lock, pdm.lock or pylock.toml) is missing.


**Decisão**: 

### 88 · ⚪ MINOR · CODE_SMELL · `python:S7504`
**Local**: `conftest.py:20` · **Effort**: 5min

> Remove this unnecessary `list()` call on an already iterable object.

```python
       16      if (
       17          existing_package is None
       18          or Path(getattr(existing_package, "__file__", "")).resolve() != init_file
       19      ):
>>>    20          for module_name in list(sys.modules):
       21              if module_name == package_name or module_name.startswith(
       22                  f"{package_name}."
       23              ):
       24                  sys.modules.pop(module_name, None)
```

**Decisão**: 

### 89 · ⚪ MINOR · CODE_SMELL · `plsql:SingleLineCommentsSyntaxCheck`
**Local**: `dbt_packages/dbt_utils/integration_tests/models/sql/test_star_aggregate.sql:1` · **Effort**: 1min

> This single line comment should use the single line comment syntax "--"

```sql
>>>     1  /*This test checks that column aliases aren't applied unless there's a prefix/suffix necessary, to ensure that GROUP BYs keep working*/
        2  
        3  {% set selected_columns = dbt_utils.star(from=ref('data_star_aggregate'), except=['value_field']) %}
        4  
        5  with data as (
```

**Decisão**: 

### 90 · ⚪ INFO · CODE_SMELL · `plsql:S1135`
**Local**: `dbt_packages/dbt_utils/integration_tests/models/sql/test_pivot.sql:2` · **Effort**: 0min

> Complete the task associated to this "TODO" comment.

```sql
        1  
>>>     2  -- TODO: How do we make this work nicely on Snowflake too?
        3  
        4  {% if target.type == 'snowflake' %}
        5      {% set column_values = ['RED', 'BLUE'] %}
        6      {% set cmp = 'ilike' %}
```

**Decisão**: 

### 91 · ⚪ INFO · CODE_SMELL · `plsql:S1135`
**Local**: `dbt_packages/dbt_utils/integration_tests/models/sql/test_pivot_apostrophe.sql:2` · **Effort**: 0min

> Complete the task associated to this "TODO" comment.

```sql
        1  
>>>     2  -- TODO: How do we make this work nicely on Snowflake too?
        3  
        4  {% if target.type == 'snowflake' %}
        5      {% set column_values = ['RED', 'BLUE', "BLUE'S"] %}
        6      {% set cmp = 'ilike' %}
```

**Decisão**: 

