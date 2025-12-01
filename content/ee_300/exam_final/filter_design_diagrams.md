# Filter Design Decision Flow Chart

```mermaid
graph TD
    Start[Filter Design Problem] --> Specs{What are your specifications?}
    
    Specs --> DefineReq[Define Requirements:<br/>- Filter Type LP/HP/BP/BS<br/>- H_MAX, H_MIN<br/>- ω_C, ω_MIN]
    
    DefineReq --> FilterType{Filter Type?}
    
    FilterType -->|Low-Pass| LPOrder[Calculate Minimum Order n]
    FilterType -->|High-Pass| HPOrder[Calculate Minimum Order n]
    FilterType -->|Band-Pass| BPDesign[Design as LP \times HP Cascade]
    FilterType -->|Band-Stop| BSDesign[Design as LP + HP Parallel]
    
    LPOrder --> PolyChoice{Polynomial Type?}
    HPOrder --> PolyChoice
    
    PolyChoice -->|Butterworth<br/>Maximally Flat| ButterworthCalc[Use Butterworth Formula:<br/>Poles on Circle]
    PolyChoice -->|Chebyshev<br/>Steeper Roll-off| ChebyshevCalc[Use Chebyshev Formula:<br/>Poles on Ellipse]
    
    ButterworthCalc --> GetPoles[Obtain Pole Locations<br/>from Tables or Formulas]
    ChebyshevCalc --> GetPoles
    
    GetPoles --> FactorH[Factor H s into<br/>1st and 2nd Order Sections]
    
    FactorH --> SectionLoop{For Each<br/>2nd Order Section}
    
    SectionLoop --> ExtractParams[Extract ζ and ω_0<br/>from Section Denominator]
    
    ExtractParams --> CheckUnityGain{Can Unity Gain<br/>μ = 1 work?}
    
    CheckUnityGain -->|Yes<br/>Always Preferred| UnityMethod[Unity Gain Method:<br/>- Set μ = 1<br/>- Works for all ζ<br/>- Calculate R and C]
    
    CheckUnityGain -->|No<br/>Special Requirement| CheckDamping{Check<br/>Damping Ratio}
    
    CheckDamping -->|0 < ζ < 1<br/>Underdamped| EqualElements[Equal Elements Method:<br/>- R1 = R2 = R<br/>- C1 = C2 = C<br/>- μ = 3 - 2ζ]
    
    CheckDamping -->|ζ \geq 1<br/>Over/Critically Damped| MustUseUnity[Must Use Unity Gain<br/>Equal Elements Invalid]
    
    MustUseUnity --> UnityMethod
    
    UnityMethod --> CalcComponents[Calculate Component Values:<br/>- Choose C1<br/>- Calculate R and C ratios<br/>- Verify practical ranges]
    
    EqualElements --> CalcComponents
    
    CalcComponents --> MoreSections{More<br/>Sections?}
    
    MoreSections -->|Yes| SectionLoop
    MoreSections -->|No| OrderSections[Order Sections:<br/>Lowest Q First<br/>Highest Q Last]
    
    OrderSections --> Cascade[Cascade Sections with<br/>Op-Amp Buffers Between Stages]
    
    Cascade --> DistributeGain[Distribute Overall Gain<br/>Across Sections if Needed]
    
    DistributeGain --> ScaleCheck{Need Frequency<br/>or Impedance Scaling?}
    
    ScaleCheck -->|Frequency Scale| FreqScale[Multiply all C by kf<br/>New ω = kf \times ω]
    ScaleCheck -->|Impedance Scale| ImpScale[Multiply R by kz<br/>Divide C by kz<br/>H s unchanged]
    ScaleCheck -->|No Scaling Needed| Verify
    
    FreqScale --> Verify[Verify Design:<br/>- Check all specs met<br/>- Op-amp GBW adequate<br/>- Component values practical]
    ImpScale --> Verify
    
    Verify --> Complete[Design Complete]
    
    BPDesign --> DesignLP[Design LP Section<br/>Follow LP Path]
    BPDesign --> DesignHP[Design HP Section<br/>Follow HP Path]
    
    DesignLP --> CombineBP[Cascade: H_BP = H_LP \times H_HP]
    DesignHP --> CombineBP
    CombineBP --> Complete
    
    BSDesign --> DesignLP2[Design LP Section<br/>Follow LP Path]
    BSDesign --> DesignHP2[Design HP Section<br/>Follow HP Path]
    
    DesignLP2 --> CombineBS[Parallel Sum: H_BS = H_LP + H_HP]
    DesignHP2 --> CombineBS
    CombineBS --> Complete
    
    style Start fill:#1976d2
    style Complete fill:#388e3c
    style UnityMethod fill:#f57c00
    style EqualElements fill:#d84315
    style CheckUnityGain fill:#c2185b
    style DefineReq fill:#7b1fa2
```

## Quick Reference: Unity Gain Method (Preferred)

### Why Unity Gain is Preferred
- Works for **all damping ratios** (ζ \geq 0)
- Simplest op-amp configuration (voltage follower)
- Zero sensitivity to gain variations
- Most stable and reliable

### Unity Gain Design Equations

**For Lowpass Sallen-Key:**
- Set μ = 1 (op-amp as buffer)
- Choose C₁ (typically 0.01 to 1 μF)
- Calculate: C₂ = (2ζ)² \times C₁
- Calculate: R₁ = R₂ = 1/(ζω₀C₁)

**For Highpass Sallen-Key:**
- Set μ = 1 (op-amp as buffer)
- Choose R₂ (typically 1k to 100k)
- Calculate: R₁ = (2ζ)² \times R₂
- Calculate: C₁ = C₂ = 1/(ζω₀R₂)

## Order Calculation Formulas

### Butterworth (Maximally Flat)

**Lowpass:**
```
n_B = ⌈ (1/2) \times log[(H_MAX/H_MIN)² - 1] / log(ω_MIN/ω_C) ⌉
```

**Highpass:**
```
n_B = ⌈ (1/2) \times log[(H_MAX/H_MIN)² - 1] / log(ω_C/ω_MIN) ⌉
```

### Chebyshev (Steeper Roll-off)

**Lowpass:**
```
n_C = ⌈ cosh-¹(√[(H_MAX/H_MIN)² - 1]) / cosh-¹(ω_MIN/ω_C) ⌉
```

**Highpass:**
```
n_C = ⌈ cosh-¹(√[(H_MAX/H_MIN)² - 1]) / cosh-¹(ω_C/ω_MIN) ⌉
```

## Key Relationships

| Parameter | Equation | Notes |
|-----------|----------|-------|
| Quality Factor | Q = 1/(2ζ) | Higher Q = more resonance |
| Damping Ratio | ζ = 1/(2Q) | Lower ζ = more peaking |
| Bandwidth | BW = 2ζω₀ = ω₀/Q | 3-dB bandwidth |
| Natural Frequency | ω₀ = 1/√(R₁R₂C₁C₂) | For Sallen-Key |

## Decision Points Summary

1. **Start:** Always begin by defining all specifications clearly
2. **Order Calculation:** Use appropriate formula for filter type and polynomial
3. **Unity Gain Check:** ALWAYS check if unity gain can work first (it usually can)
4. **Equal Elements:** Only use if μ > 1 is required AND 0 < ζ < 1
5. **Section Ordering:** Low Q (high ζ) sections first, high Q (low ζ) last
6. **Scaling:** Apply frequency and impedance scaling to get practical component values

## Common Damping Values

| Response Type | ζ | Q | Characteristics |
|---------------|---|---|-----------------|
| Butterworth | 0.707 | 0.707 | Maximally flat, -3dB at ω₀ |
| Chebyshev 0.5dB | ~0.86 | ~0.58 | Slight ripple, sharp transition |
| Chebyshev 1dB | ~0.52 | ~0.96 | More ripple, sharper transition |
| Bessel | 0.866 | 0.577 | Linear phase, minimal overshoot |
| Critically Damped | 1.0 | 0.5 | No overshoot, fastest settling |