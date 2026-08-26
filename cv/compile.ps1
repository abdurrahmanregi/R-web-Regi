# Compile the CV and copy the PDF to static/ so Hugo serves it at the existing URL.
$ErrorActionPreference = "Stop"

$CvDir = $PSScriptRoot
$RepoRoot = Split-Path -Parent $CvDir
$OutDir = Join-Path $CvDir "build"
$PdfSrc = Join-Path $OutDir "kusumaatmadja_cv.pdf"
$PdfDest = Join-Path $RepoRoot "static\kusumaatmadja_cv_tinbergen.pdf"

New-Item -ItemType Directory -Force -Path $OutDir | Out-Null

Push-Location $CvDir
try {
  & python "$CvDir\extract_papers.py"
  if ($LASTEXITCODE -ne 0) {
    throw "extract_papers.py failed with exit code $LASTEXITCODE"
  }
  # Two pdflatex passes so hyperref links resolve. Avoids latexmk, which needs Perl.
  foreach ($pass in 1..2) {
    & pdflatex -interaction=nonstopmode -halt-on-error -output-directory=build kusumaatmadja_cv.tex
    if ($LASTEXITCODE -ne 0) {
      throw "pdflatex pass $pass failed with exit code $LASTEXITCODE"
    }
  }
} finally {
  Pop-Location
}

if (-not (Test-Path $PdfSrc)) {
  throw "Expected PDF was not produced: $PdfSrc"
}

Copy-Item -Force $PdfSrc $PdfDest
Write-Host "Wrote $PdfDest"
