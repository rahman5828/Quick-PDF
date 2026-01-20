async function mergePDFs() {
  const input = document.getElementById("files");
  const status = document.getElementById("status");

  if (input.files.length < 2) {
    status.innerText = "❌ Please select at least 2 PDF files.";
    return;
  }

  status.innerText = "⏳ Merging PDFs...";

  const formData = new FormData();
  for (const file of input.files) {
    formData.append("files", file);
  }

  try {
    const response = await fetch("/merge", {
      method: "POST",
      body: formData
    });

    if (!response.ok) throw new Error("Merge failed");

    const blob = await response.blob();
    const url = window.URL.createObjectURL(blob);

    const a = document.createElement("a");
    a.href = url;
    a.download = "merged.pdf";
    document.body.appendChild(a);
    a.click();
    a.remove();

    status.innerText = "✅ Download started!";
  } catch (err) {
    status.innerText = "❌ Error merging PDFs.";
  }
}
