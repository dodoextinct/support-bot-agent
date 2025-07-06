from flask import Blueprint, request, jsonify
from workflows.support_workflow import SupportWorkflow

support_bp = Blueprint("support_bp", __name__)


@support_bp.route("/support", methods=["POST"])
def handle_support():
    try:
        body = request.get_json()
        prompt = body.get("prompt", "")
        if not prompt:
            return jsonify({"error": "Missing prompt"}), 400

        workflow = SupportWorkflow(session_id="support-session")
        response_iter = workflow.run_workflow(prompt)

        for response in response_iter:
            return jsonify(response.content)

        return jsonify({"error": "No response generated"}), 500

    except Exception as e:
        print(f"[ERROR] /support route: {e}")
        return jsonify({"error": str(e)}), 500
