from pathlib import Path

from youtube_transcript_api import YouTubeTranscriptApi


VIDEOS = {
    "aircAruvnKk": "3blue1brown_neural_network",
    "wjZofJX0v4M": "3blue1brown_transformers",
    "fHF22Wxuyw4": "campusx_deep_learning_hindi",
    "C6YtPJxNULA": "codewithharry_ml_deep_learning_hindi",
}


def fetch_and_save(video_id: str, output_name: str, output_dir: Path) -> None:
    api = YouTubeTranscriptApi()
    transcript = api.fetch(video_id, languages=("en", "hi"))
    lines = []
    for row in transcript:
        start = getattr(row, "start", 0.0)
        text = getattr(row, "text", "").replace("\n", " ").strip()
        lines.append(f"[{start:8.2f}s] {text}")
    output_path = output_dir / f"{output_name}.txt"
    output_path.write_text("\n".join(lines), encoding="utf-8")
    print(f"Saved: {output_path}")


def main() -> None:
    root_dir = Path(__file__).resolve().parents[1]
    output_dir = root_dir / "transcripts"
    output_dir.mkdir(parents=True, exist_ok=True)

    for video_id, output_name in VIDEOS.items():
        try:
            fetch_and_save(video_id, output_name, output_dir)
        except Exception as exc:
            print(f"Failed for {video_id}: {exc}")


if __name__ == "__main__":
    main()
