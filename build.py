"""Build index.html from src/promos.src.html, inlining the Paralucent heading font."""
import base64, pathlib
root = pathlib.Path(__file__).parent
src = (root / "src/promos.src.html").read_text()
faces = []
for w in (500, 600, 700):
    b64 = base64.b64encode((root / f"assets/paralucent-{w}.woff2").read_bytes()).decode()
    faces.append(f'@font-face{{font-family:"paralucent";src:url(data:font/woff2;base64,{b64}) format("woff2");font-weight:{w};font-style:normal;font-display:swap}}')
(root / "index.html").write_text(src.replace("/*PARALUCENT*/", "\n".join(faces), 1))
print("built", len(src))
