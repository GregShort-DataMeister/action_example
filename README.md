# Simple GitHub Actions Demonstration

This repository contains:
- A GitHub Actions workflow (`.github/workflows/execute.yml`) that simply prints **Executed**.
- A Python script (`trigger_workflow.py`) that uses GitHub's REST API to dispatch this workflow.

## How to Use

1. **Fork this repository** into your own GitHub account.
2. Clone your fork locally.
3. **Enable GitHub Actions in Your Fork** (Required for workflows to run):
   - Go to **Settings** → **Actions** in your forked repo.
   - Under **"Workflow permissions"**, select **Read and write permissions**.
   - Under **"Fork pull request workflows"**, select **"Require approval for all outside collaborators"** (or enable auto-run).
   - Click **Save**.
4. **Create a Personal Access Token (PAT)**:
   - Go to [GitHub Developer Settings](https://github.com/settings/tokens).
   - Click **Generate new token (classic)** (or use a Fine-grained token).
   - **Scopes Required**:
     - `repo` → Full control of repositories (needed to access the repo)
     - `workflow` → Allows triggering workflows
   - Generate the token and copy it (you won’t see it again).
5. Install dependencies locally:
   ```bash
   pip install requests
   ```
6. Run the Python script to dispatch the workflow:
   ```bash
   python trigger_workflow.py --repo YOUR_GITHUB_USERNAME/YOUR_FORK_NAME --token YOUR_TOKEN
   ```
   - By default, it will trigger the workflow named `execute.yml` on the `main` branch.

7. Check the **Actions** tab in your repository after running the script to see the workflow run. You should see "Executed" in the logs.

## Security Considerations
- **Limited Permissions**: A forked repository cannot push back to the original, preventing unwanted modifications.
- **Scoped Token**: If using a Fine-Grained PAT, ensure it has **repo → actions** permissions.
- **Approval for External Workflows**: By default, workflows in forks require approval from a repository maintainer before running.

After completing these steps, your workflow should run successfully!

