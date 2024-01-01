// 异步加载Markdown文件内容并渲染
async function loadAndRenderMarkdown(markdownPath) {
    try {
        const response = await fetch(markdownPath);
        if (!response.ok) {
            throw new Error(`Failed to fetch ${markdownPath}`);
        }

        const markdownText = await response.text();
        // 将Markdown内容渲染到div中
        document.getElementById('markdownContent').innerHTML = marked(markdownText);
    } catch (error) {
        console.error('Error:', error);
    }
}