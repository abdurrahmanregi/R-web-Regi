# Compile the CV and research statement, then copy the PDFs to static/.
$ErrorActionPreference = "Stop"

$CvDir = $PSScriptRoot
$RepoRoot = Split-Path -Parent $CvDir
$OutDir = Join-Path $CvDir "build"

New-Item -ItemType Directory -Force -Path $OutDir | Out-Null

function Invoke-PdfLatex([string]$TexFile) {
  foreach ($pass in 1..2) {
    & pdflatex -interaction=nonstopmode -halt-on-error -output-directory=build $TexFile
    if ($LASTEXITCODE -ne 0) {
      throw "pdflatex $TexFile pass $pass failed with exit code $LASTEXITCODE"
    }
  }
}

function Copy-BuiltPdf([string]$BuiltName, [string]$DestName) {
  $src = Join-Path $OutDir $BuiltName
  $dest = Join-Path $RepoRoot "static\$DestName"
  if (-not (Test-Path $src)) {
    throw "Expected PDF was not produced: $src"
  }
  Copy-Item -Force $src $dest
  Write-Host "Wrote $dest"
}

Push-Location $CvDir
try {
  & python "$CvDir\extract_papers.py"
  if ($LASTEXITCODE -ne 0) {
    throw "extract_papers.py failed with exit code $LASTEXITCODE"
  }
  # Two pdflatex passes so hyperref links resolve. Avoids latexmk, which needs Perl.
  Invoke-PdfLatex "kusumaatmadja_cv.tex"
  Invoke-PdfLatex "kusumaatmadja_researchstatement.tex"
} finally {
  Pop-Location
}

Copy-BuiltPdf "kusumaatmadja_cv.pdf" "kusumaatmadja_cv_tinbergen.pdf"
Copy-BuiltPdf "kusumaatmadja_researchstatement.pdf" "kusumaatmadja_researchstatement.pdf"
