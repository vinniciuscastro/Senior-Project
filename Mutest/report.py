"""
Report generation module for Mutest mutation testing tool.
Supports text, HTML, and JSON report formats.
"""
from datetime import datetime
import json


def generate_text_report(results, output_file, source_file, test_command):
    """Generate a detailed text report of mutation testing results"""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write("=" * 70 + "\n")
        f.write("MUTEST - MUTATION TESTING REPORT\n")
        f.write("=" * 70 + "\n\n")

        f.write(f"Generated: {timestamp}\n")
        f.write(f"Source File: {source_file}\n")
        f.write(f"Test Command: {test_command}\n\n")

        f.write("=" * 70 + "\n")
        f.write("SUMMARY\n")
        f.write("=" * 70 + "\n\n")

        f.write(f"Total Mutants:    {results['total']}\n")
        f.write(f"Killed:           {results['killed_count']} ({results['killed_count']/results['total']*100:.1f}%)\n")
        f.write(f"Survived:         {results['survived_count']} ({results['survived_count']/results['total']*100:.1f}%)\n")
        f.write(f"Timeout:          {results['timeout_count']} ({results['timeout_count']/results['total']*100:.1f}%)\n\n")

        score = results['mutation_score']
        f.write(f"Mutation Score:   {score:.2f}%\n\n")

        # Quality assessment
        if score >= 97:
            f.write("Quality Assessment: EXCELLENT ✓\n")
        elif score >= 90:
            f.write("Quality Assessment: GOOD\n")
        elif score >= 80:
            f.write("Quality Assessment: FAIR\n")
        else:
            f.write("Quality Assessment: POOR ✗\n")

        f.write("\n")

        # Killed mutants
        if results['killed']:
            f.write("=" * 70 + "\n")
            f.write(f"KILLED MUTANTS ({len(results['killed'])})\n")
            f.write("=" * 70 + "\n\n")

            for mutant in results['killed']:
                info = mutant['mutation_info']
                f.write(f"Mutant #{mutant['mutant_number']}:\n")
                f.write(f"  Type:     {info['type']}\n")
                f.write(f"  Location: Line {info['line']}, Column {info['col']}\n")
                f.write(f"  Change:   {info['original']} → {info['mutated']}\n")
                f.write(f"  Status:   KILLED ✓\n\n")

        # Survived mutants (these are important!)
        if results['survived']:
            f.write("=" * 70 + "\n")
            f.write(f"SURVIVED MUTANTS ({len(results['survived'])}) - ACTION NEEDED!\n")
            f.write("=" * 70 + "\n\n")

            f.write("These mutants were not detected by your tests. Consider adding\n")
            f.write("test cases to cover these scenarios:\n\n")

            for mutant in results['survived']:
                info = mutant['mutation_info']
                f.write(f"Mutant #{mutant['mutant_number']}:\n")
                f.write(f"  Type:     {info['type']}\n")
                f.write(f"  Location: Line {info['line']}, Column {info['col']}\n")
                f.write(f"  Change:   {info['original']} → {info['mutated']}\n")
                f.write(f"  Status:   SURVIVED ✗\n")
                f.write(f"  Action:   Add test case to detect this mutation\n\n")

        # Timeout mutants
        if results['timeout']:
            f.write("=" * 70 + "\n")
            f.write(f"TIMEOUT MUTANTS ({len(results['timeout'])})\n")
            f.write("=" * 70 + "\n\n")

            for mutant in results['timeout']:
                info = mutant['mutation_info']
                f.write(f"Mutant #{mutant['mutant_number']}:\n")
                f.write(f"  Type:     {info['type']}\n")
                f.write(f"  Location: Line {info['line']}, Column {info['col']}\n")
                f.write(f"  Change:   {info['original']} → {info['mutated']}\n")
                f.write(f"  Status:   TIMEOUT ⏱\n\n")

        f.write("=" * 70 + "\n")
        f.write("END OF REPORT\n")
        f.write("=" * 70 + "\n")


def generate_html_report(results, output_file, source_file, test_command):
    """Generate an interactive HTML report of mutation testing results"""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    score = results['mutation_score']

    # Determine score color
    if score >= 97:
        score_class = "excellent"
        score_label = "EXCELLENT"
    elif score >= 90:
        score_class = "good"
        score_label = "GOOD"
    elif score >= 80:
        score_class = "fair"
        score_label = "FAIR"
    else:
        score_class = "poor"
        score_label = "POOR"

    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Mutest Report - {source_file}</title>
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}

        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            padding: 2rem;
            min-height: 100vh;
        }}

        .container {{
            max-width: 1200px;
            margin: 0 auto;
            background: white;
            border-radius: 12px;
            box-shadow: 0 20px 60px rgba(0,0,0,0.3);
            overflow: hidden;
        }}

        .header {{
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 2rem;
            text-align: center;
        }}

        .header h1 {{
            font-size: 2.5rem;
            margin-bottom: 0.5rem;
        }}

        .header p {{
            opacity: 0.9;
            font-size: 1.1rem;
        }}

        .content {{
            padding: 2rem;
        }}

        .meta-info {{
            background: #f8f9fa;
            padding: 1.5rem;
            border-radius: 8px;
            margin-bottom: 2rem;
        }}

        .meta-info div {{
            margin: 0.5rem 0;
        }}

        .meta-info strong {{
            display: inline-block;
            width: 150px;
            color: #495057;
        }}

        .score-card {{
            text-align: center;
            padding: 2rem;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            border-radius: 8px;
            margin-bottom: 2rem;
            color: white;
        }}

        .score-value {{
            font-size: 4rem;
            font-weight: bold;
            margin: 1rem 0;
        }}

        .score-label {{
            font-size: 1.5rem;
            opacity: 0.9;
        }}

        .stats-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 1rem;
            margin-bottom: 2rem;
        }}

        .stat-card {{
            padding: 1.5rem;
            border-radius: 8px;
            text-align: center;
        }}

        .stat-card.killed {{
            background: #d4edda;
            border-left: 4px solid #28a745;
        }}

        .stat-card.survived {{
            background: #f8d7da;
            border-left: 4px solid #dc3545;
        }}

        .stat-card.timeout {{
            background: #fff3cd;
            border-left: 4px solid #ffc107;
        }}

        .stat-value {{
            font-size: 2rem;
            font-weight: bold;
            margin-bottom: 0.5rem;
        }}

        .stat-label {{
            color: #6c757d;
            font-size: 0.9rem;
        }}

        .section {{
            margin-bottom: 2rem;
        }}

        .section-title {{
            font-size: 1.5rem;
            margin-bottom: 1rem;
            padding-bottom: 0.5rem;
            border-bottom: 2px solid #dee2e6;
            color: #495057;
        }}

        .mutant-card {{
            background: #f8f9fa;
            border-left: 4px solid #6c757d;
            padding: 1rem;
            margin-bottom: 1rem;
            border-radius: 4px;
        }}

        .mutant-card.killed {{
            border-left-color: #28a745;
        }}

        .mutant-card.survived {{
            border-left-color: #dc3545;
            background: #fff5f5;
        }}

        .mutant-card.timeout {{
            border-left-color: #ffc107;
        }}

        .mutant-header {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 0.5rem;
        }}

        .mutant-number {{
            font-weight: bold;
            color: #495057;
        }}

        .mutant-status {{
            padding: 0.25rem 0.75rem;
            border-radius: 4px;
            font-size: 0.85rem;
            font-weight: bold;
        }}

        .mutant-status.killed {{
            background: #28a745;
            color: white;
        }}

        .mutant-status.survived {{
            background: #dc3545;
            color: white;
        }}

        .mutant-status.timeout {{
            background: #ffc107;
            color: #000;
        }}

        .mutant-detail {{
            margin: 0.25rem 0;
            color: #6c757d;
            font-size: 0.9rem;
        }}

        .mutation-change {{
            font-family: 'Courier New', monospace;
            background: white;
            padding: 0.5rem;
            border-radius: 4px;
            margin-top: 0.5rem;
        }}

        .mutation-change .original {{
            color: #dc3545;
            text-decoration: line-through;
        }}

        .mutation-change .mutated {{
            color: #28a745;
            font-weight: bold;
        }}

        .footer {{
            text-align: center;
            padding: 2rem;
            background: #f8f9fa;
            color: #6c757d;
            font-size: 0.9rem;
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>🧬 Mutest Report</h1>
            <p>Mutation Testing Results</p>
        </div>

        <div class="content">
            <div class="meta-info">
                <div><strong>Generated:</strong> {timestamp}</div>
                <div><strong>Source File:</strong> {source_file}</div>
                <div><strong>Test Command:</strong> {test_command}</div>
            </div>

            <div class="score-card">
                <div class="score-label">Mutation Score</div>
                <div class="score-value">{score:.1f}%</div>
                <div class="score-label">{score_label}</div>
            </div>

            <div class="stats-grid">
                <div class="stat-card killed">
                    <div class="stat-value">{results['killed_count']}</div>
                    <div class="stat-label">Mutants Killed</div>
                </div>
                <div class="stat-card survived">
                    <div class="stat-value">{results['survived_count']}</div>
                    <div class="stat-label">Mutants Survived</div>
                </div>
                <div class="stat-card timeout">
                    <div class="stat-value">{results['timeout_count']}</div>
                    <div class="stat-label">Timeouts</div>
                </div>
            </div>

            {'<div class="section"><h2 class="section-title">🎯 Killed Mutants (' + str(len(results['killed'])) + ')</h2>' + ''.join([f'''
                <div class="mutant-card killed">
                    <div class="mutant-header">
                        <span class="mutant-number">Mutant #{mutant['mutant_number']}</span>
                        <span class="mutant-status killed">KILLED</span>
                    </div>
                    <div class="mutant-detail"><strong>Type:</strong> {mutant['mutation_info']['type']}</div>
                    <div class="mutant-detail"><strong>Location:</strong> Line {mutant['mutation_info']['line']}, Column {mutant['mutation_info']['col']}</div>
                    <div class="mutation-change">
                        <span class="original">{mutant['mutation_info']['original']}</span> → <span class="mutated">{mutant['mutation_info']['mutated']}</span>
                    </div>
                </div>
            ''' for mutant in results['killed']]) + '</div>' if results['killed'] else ''}

            {'<div class="section"><h2 class="section-title">⚠️ Survived Mutants (' + str(len(results['survived'])) + ') - Action Needed!</h2>' + ''.join([f'''
                <div class="mutant-card survived">
                    <div class="mutant-header">
                        <span class="mutant-number">Mutant #{mutant['mutant_number']}</span>
                        <span class="mutant-status survived">SURVIVED</span>
                    </div>
                    <div class="mutant-detail"><strong>Type:</strong> {mutant['mutation_info']['type']}</div>
                    <div class="mutant-detail"><strong>Location:</strong> Line {mutant['mutation_info']['line']}, Column {mutant['mutation_info']['col']}</div>
                    <div class="mutation-change">
                        <span class="original">{mutant['mutation_info']['original']}</span> → <span class="mutated">{mutant['mutation_info']['mutated']}</span>
                    </div>
                    <div style="margin-top: 0.5rem; color: #721c24; font-size: 0.9rem;">
                        ⚠️ Add test case to detect this mutation
                    </div>
                </div>
            ''' for mutant in results['survived']]) + '</div>' if results['survived'] else ''}

            {'<div class="section"><h2 class="section-title">⏱️ Timeout Mutants (' + str(len(results['timeout'])) + ')</h2>' + ''.join([f'''
                <div class="mutant-card timeout">
                    <div class="mutant-header">
                        <span class="mutant-number">Mutant #{mutant['mutant_number']}</span>
                        <span class="mutant-status timeout">TIMEOUT</span>
                    </div>
                    <div class="mutant-detail"><strong>Type:</strong> {mutant['mutation_info']['type']}</div>
                    <div class="mutant-detail"><strong>Location:</strong> Line {mutant['mutation_info']['line']}, Column {mutant['mutation_info']['col']}</div>
                    <div class="mutation-change">
                        <span class="original">{mutant['mutation_info']['original']}</span> → <span class="mutated">{mutant['mutation_info']['mutated']}</span>
                    </div>
                </div>
            ''' for mutant in results['timeout']]) + '</div>' if results['timeout'] else ''}
        </div>

        <div class="footer">
            Generated by Mutest v0.0.1 • {timestamp}
        </div>
    </div>
</body>
</html>"""

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(html_content)


def generate_json_report(results, output_file, source_file, test_command):
    """Generate a JSON report for programmatic access"""
    timestamp = datetime.now().isoformat()

    report_data = {
        "metadata": {
            "generated_at": timestamp,
            "source_file": source_file,
            "test_command": test_command,
            "mutest_version": "0.0.1"
        },
        "summary": {
            "total_mutants": results['total'],
            "killed_count": results['killed_count'],
            "survived_count": results['survived_count'],
            "timeout_count": results['timeout_count'],
            "mutation_score": round(results['mutation_score'], 2)
        },
        "mutants": {
            "killed": results['killed'],
            "survived": results['survived'],
            "timeout": results['timeout']
        }
    }

    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(report_data, f, indent=2, ensure_ascii=False)
