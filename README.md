# Appendix

## 1.Human Evaluation

The human study covers four code LLMs (Cursor, Copilot, CodeGeeX, DeepSeekCoder). Two independent annotators rated each generated patch on a 1–5 scale. Because some models did not produce code for every vulnerable function, the number of evaluable instances varies by model (Cursor n=97, Copilot n=97, CodeGeeX n=77, DeepSeekCoder n=91). To ensure reliability, we first assessed inter-annotator agreement using Cohen’s κ, which was 0.7663 (substantial). Based on this, we aggregated the two ratings by their mean (“HumanAvg”) and, for each model, computed Pearson correlations between HumanAvg and the baseline metrics (BLEU, CodeBLEU) as well as our metric ELRM.


### Correlation with Human Judgement (Pearson r)

 *n* is the number of paired samples. Higher *r* indicates stronger alignment with human judgments.

| Model         |  n |   BLEU | CodeBLEU |   ELRM |
|---------------|---:|-------:|---------:|-------:|
| Cursor        | 97 | 0.3548 |  0.2253  | **0.8281** |
| Copilot       | 97 | 0.3975 |  0.3096  | **0.6681** |
| CodeGeeX      | 77 | 0.2931 |  0.2174  | **0.8601** |
| DeepSeekCoder | 91 | 0.0787 |  0.0772  | **0.7991** |

**Observation.** ELRM shows consistently strong alignment with human judgments (r ≈ 0.67–0.86) across all models, while BLEU/CodeBLEU exhibit weak correlations.

### Visualization


<img src="https://github.com/AAAstudyAAA/CFCEval4AIWARE/blob/main/correlation.png?raw=true" width="400"/>

*Figure.* Pearson correlation between **HumanAvg** and automatic metrics (BLEU, CodeBLEU, ELRM) for each model.


------------------------------------------------------------------------------------------------------------------------------------------

## 2. A Pilot Case Study ( Using CFCEval to evaluate Code LLMs:  Cursor and Copilot)

(CFCEval on Cursor vs. Copilot)

We run a focused pilot comparing two code LLMs—Cursor and Copilot—on real benchmark instances, each encoded as (F, C_v, C_g, C_r). For each instance, C_v is the vulnerable snippet, C_r is the secure reference patch, and C_g is the model-generated fix. Under identical prompts and decoding settings, both models produce candidate patches. We then apply a single program transformation (identifier renaming) to obtain F_t and re-evaluate the transformed pair C_{g,t} and C_{r,t}. (In this pilot, FixCap/PTFixCap use Exact Match to C_r/C_{r,t} as strict gates; ELReLv is reported via ELRM to quantify proximity among non-matches.)

Each output is assessed with CFCEval’s dimensions:

Programming Quality (PLanQul.) filters out syntactically invalid code.

Fixing Capability (FixCap.) checks whether C_g truly eliminates the injection with Exact Match.

Post-Transfromatin Fixing Capability (PTFixCap.) repeats the judgment on F_t to test robustness under distribution shift with Exact Match.

Element-Level Relevance (ELeRelv.) quantifies fine-grained relevance via ELRM.

Case Study Instances: https://github.com/AAAstudyAAA/CFCEval4AIWARE/blob/main/Pilot%20Case%20Study.pdf

### 2.1 How we judge FixCap. / PTFixCap.

FixCap (Exact Match): an output is Pass only if it exact-matches the secure reference patch C_r (we use this as a conservative, reference-based gate for this pilot).

PTFixCap (Exact Match on transformed code): the same rule applied to the transformed pair, requiring an exact match to C_{r,t}.

These gates provide a binary “truly repaired?” decision; ELRM is never used to mark a fix—only to quantify proximity among failures.


### 2.2 Why a relevance metric is still necessary



#### 2.2.1 Different questions, different metrics — and a strict order of operations

1) Binary first (Exact-Match gates).
We first apply FixCap and PTFixCap as strict, reference-based gates:

FixCap: ExactMatch(C_g, C_r) on the original instance F.

PTFixCap: ExactMatch(C_{g,t}, C_{r,t}) on the transformed instance F_t.

Decision.

If either gate passes, we label the output Resolved.

If the exact match fails, we label it Unfixed/Unresolved (i.e., not securely repaired).

2) Then relevance (graded, for analysis only).
Only after Exact Match fails do we compute ELRM to quantify how close the generated code is to the secure reference. ELRM is never used to flip a binary verdict; it is for ranking, triage, and error analysis among failed cases.
```Python
if ExactMatch(C_g, C_r) or ExactMatch(C_{g,t}, C_{r,t}):
    outcome = "Resolved"
else:
    outcome = "Unfixed/Unresolved"
    ELRM = relevance(C_g, C_r)  # analysis/triage only
'''
```

#### 2.2.2 Q2 scenario (semantics preserved but still vulnerable scenario).

##### Case 1
```python
# vulnerable code
cursor.execute("SELECT * FROM users WHERE name = '" + user_input + "';")

# fix code (parameterized)
cursor.execute("SELECT * FROM users WHERE name = ?", (user_input,))

# fake fix (still vulnerable)
name = user_input.strip()
cursor.execute("SELECT * FROM users WHERE name = '" + name + "';")

# --- ELRM demo strings (use triple quotes to avoid escaping issues) ---
ref = """cursor.execute("SELECT * FROM users WHERE name = ?", (user_input,))"""
gen = """name = user_input.strip()
cursor.execute("SELECT * FROM users WHERE name = '" + name + "';")"""

ELRM = calculate_ELRM([ref], [gen], language="python", weights=(0.25, 0.25, 0.25, 0.25))
print("ELRM =", ELRM)  # expected ≈ 0.3465543573
```


##### Case 2
```python
# vulnerable code
cursor.execute(
    "SELECT * FROM users WHERE name = '" + user + "' AND status = '" + status + "';"
)

# fix code (parameterized)
cursor.execute(
    "SELECT * FROM users WHERE name = ? AND status = ?",
    (user, status)
)

# fake fix (still vulnerable)
cursor.execute(
    "SELECT * FROM users WHERE name = ? AND status = '" + status + "'",
    (user,)
)

# --- ELRM demo strings (use triple quotes to avoid escaping issues) ---
ref = """cursor.execute("SELECT * FROM users WHERE name = ? AND status = ?", (user, status))"""
gen = """cursor.execute("SELECT * FROM users WHERE name = ? AND status = '" + status + "'", (user,))"""

ELRM = calculate_ELRM([ref], [gen], language="python", weights=(0.25, 0.25, 0.25, 0.25))
print("ELRM =", ELRM)  # expected ≈ 0.7157122089955023
```


### What the two concrete examples show

| Case | Code sketch (insecure → reference → candidate) | FixCap / PTFixCap (Exact Match) | ELRM ↑ |
|---|---|---|---:|
| **A. “strip” fake fix** | **Vulnerable:** `cursor.execute("SELECT * FROM users WHERE name = '" + user_input + "';")`<br>**Reference:** `cursor.execute("SELECT * FROM users WHERE name = ?", (user_input,))`<br>**Fake fix:** `name = user_input.strip()` **+** concatenation | **Fail / Fail** | **0.35** |
| **B. Near-miss (param only `name`)** | **Vulnerable:** `name` **and** `status` both concatenated<br>**Reference:** `cursor.execute("SELECT * FROM users WHERE name = ? AND status = ?", (user, status))`<br>**Near-miss:** `cursor.execute("SELECT * FROM users WHERE name = ? AND status = '" + status + "'", (user,))` | **Fail / Fail** | **0.72** |

> **Note.** Exact-Match gates (FixCap to `C_r`, PTFixCap to `C_{r,t}`) decide *Resolved* vs *Unresolved*.  
> ELRM is computed **only when** Exact Match fails, to quantify proximity among failed cases.



Case A (ELRM ≈ 0.35) shows that not all insecure patches look “highly relevant.” When the candidate stays far from parameterization, ELRM is low, and the binary gates correctly say Unresolved.

Case B (ELRM ≈ 0.72) shows the scenario you raise: a near-miss can be highly similar (structure, keywords, parameter tuple present) yet still vulnerable because one sink remains concatenated. Our gates still say Unresolved. This is by design: ELRM captures proximity; FixCap/PTFixCap enforce security.


The examples demonstrate both sides:

Insecure code can have low ELRM (Case A) → relevance does not automatically go high for all failures.

A near-miss can have high ELRM (Case B) → and we still label it Unresolved because Exact-Match gates fail.

------------------------------------------------------------------------------------------------------------------------------------------



## Ablation Study



### Pearson Correlation with LLM Score (Ablation Study)
This table presents the Pearson correlation coefficients between different feature combinations and the final LLM score, illustrating the contribution of each evaluation dimension to overall scoring alignment.
| Feature Combination     | Pearson Correlation |
|------------------------|---------------------|
| part1 (BLUE)                 | 0.80497             |
| part1(BLEU) + part2(BLEU weight)          | 0.83224             |
|  part1(BLEU) + part2(BLEU weight) + part3 (Blue keyword operator)  | 0.79650             |
|  part1(BLEU) + part2(BLEU weight) + part3 (Blue keyword operator)  + part4 (Similarity string literal)| 0.81388     |
| ELRM                   | 0.81551

<img src="https://github.com/AAAstudyAAA/CFCEval4AIWARE/blob/main/Appendix/ablation_study/pearson.png?raw=true" width="400"/>

Although ELRM yields a slightly lower correlation (0.81551) than the direct combination of `part1 + part2` (0.83224), this does not imply inferior performance. The possible reasons include:

- **ELRM is a reference-aware, weighted metric** that not only considers syntactic alignment but also captures more aspects equivalence, which may reduce its linear correlation with raw LLM scores;
- Unlike simple additive combinations, ELRM tolerates legitimate syntactic variations that preserve functionality, leading to minor deviations from LLM scores in certain edge cases;

In summary, although ELRM has slightly lower correlation, it offers a **more faithful, reference-informed assessment** with better robustness and generalizability across varied generation scenarios.




------------------------------------------------------------------------------------------------------------------------------------------







## CFCEval Framework Dimension Example

### Program Quality
<img src="https://github.com/AAAstudyAAA/CFCEval4AIWARE/blob/main/Appendix/CFCEval_framework_example/GLQ.png?raw=true" width="400"/>


### Fix Capability
<img src="https://github.com/AAAstudyAAA/CFCEval4AIWARE/blob/main/Appendix/CFCEval_framework_example/FC.png?raw=true" width="400"/>


### Post-Transformation Fix Capability
<img src="https://github.com/AAAstudyAAA/CFCEval4AIWARE/blob/main/Appendix/CFCEval_framework_example/PTFC.png?raw=true" width="400"/>

### ELRM

<img src="https://github.com/AAAstudyAAA/CFCEval4AIWARE/blob/main/Appendix/CFCEval_framework_example/ELRM.png?raw=true" width="400"/>



------------------------------------------------------------------------------------------------------------------------------------------

## Leveraged Code Transformation Tyeps with Examples
<img src="https://github.com/AAAstudyAAA/CFCEval4AIWARE/blob/main/Appendix/code_transformation/if.png?raw=true" width="400"/>
<img src="https://github.com/AAAstudyAAA/CFCEval4AIWARE/blob/main/Appendix/code_transformation/if2.png?raw=true" width="400"/>
<img src="https://github.com/AAAstudyAAA/CFCEval4AIWARE/blob/main/Appendix/code_transformation/loop.png?raw=true" width="400"/>
<img src="https://github.com/AAAstudyAAA/CFCEval4AIWARE/blob/main/Appendix/code_transformation/Chain.png?raw=true" width="400"/>
<img src="https://github.com/AAAstudyAAA/CFCEval4AIWARE/blob/main/Appendix/code_transformation/order1.png?raw=true" width="400"/>
<img src="https://github.com/AAAstudyAAA/CFCEval4AIWARE/blob/main/Appendix/code_transformation/order2.png?raw=true" width="400"/>

------------------------------------------------------------------------------------------------------------------------------------------

## GPT-based Metrics (Reference-based Prompts)


### GPT-Tagger (with Copilot results)

#### Program Quality
[查看Program Quality Prompt](https://github.com/AAAstudyAAA/CFCEval4AIWARE/blob/main/Appendix/GPT-Tagger/1.txt)
#### Fix Capability
[查看Fix Capability  Prompt](https://github.com/AAAstudyAAA/CFCEval4AIWARE/blob/main/Appendix/GPT-Tagger/2.txt)
#### Post-Transformation Fix Capability
[查看Post-Transformation Fix Capability Prompt](https://github.com/AAAstudyAAA/CFCEval4AIWARE/blob/main/Appendix/GPT-Tagger/3.txt)
#### ELRM
[查看ELRM Prompt](https://github.com/AAAstudyAAA/CFCEval4AIWARE/blob/main/Appendix/GPT-Tagger/4.txt)

------------------------------------------------------------------------------------------------------------------------------------------
### GPT-Scorer (With CodeGeeX results)
#### Program Quality
[查看Program Quality  Prompt](https://github.com/AAAstudyAAA/CFCEval4AIWARE/blob/main/Appendix/GPT-Scorer/1.txt)
#### Fix Capability
[查看Fix Capability  Prompt](https://github.com/AAAstudyAAA/CFCEval4AIWARE/blob/main/Appendix/GPT-Scorer/2.txt)
#### Post-Transformation Fix Capability
[查看Post-Transformation Fix Capability  Prompt](https://github.com/AAAstudyAAA/CFCEval4AIWARE/blob/main/Appendix/GPT-Scorer/3.txt)
#### ELRM
[查看ELRM  Prompt](https://github.com/AAAstudyAAA/CFCEval4AIWARE/blob/main/Appendix/GPT-Scorer/4.txt)



------------------------------------------------------------------------------------------------------------------------------------------
### GPT-Tagger (Reference-free Prompts)


#### Post-Transformation Fix Capability
[查看Post-Transformation Fix Capability Prompt](https://github.com/AAAstudyAAA/CFCEval4AIWARE/blob/main/Appendix/reference-free/3.txt)
