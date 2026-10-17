import argparse
import sys
from core_pipeline import BridgePipeline
from utils import read_source_file, write_output_file, console

def main():
    parser = argparse.ArgumentParser(description="Argon-Opus Architectural Bridge Code Generator")
    parser.add_argument("--prompt", type=str, required=True, help="The specification of what you want to build/refactor.")
    parser.add_argument("--input", type=str, default="", help="Optional path to local legacy file to pass as context.")
    parser.add_argument("--output", type=str, required=True, help="Path where the final polished production code will be saved.")

    args = parser.parse_args()

    try:
        legacy_material = ""
        if args.input:
            console.print(f"[bold gray]Reading legacy input file: {args.input}[/bold gray]")
            legacy_material = read_source_file(args.input)

        # Initialize the pipeline
        pipeline = BridgePipeline()

        # Step 1: Run through Gemini 4 Argon
        raw_blueprint = pipeline.execute_argon_prototype(args.prompt, legacy_material)

        # Step 2: Refine with Claude Opus 5.5
        polished_production_code = pipeline.execute_opus_refinement(args.prompt, raw_blueprint)

        # Save Final Deliverable
        write_output_file(args.output, polished_production_code)
        console.print(f"\n[bold green]✔ Success![/bold green] Production-grade software written to: [bold white]{args.output}[/bold white]\n")

    except Exception as e:
        console.print(f"\n[bold red]Pipeline Execution Failed:[/bold red] {str(e)}", style="red")
        sys.exit(1)

if __name__ == "__main__":
    main()
