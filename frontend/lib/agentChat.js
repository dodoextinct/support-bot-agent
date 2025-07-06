export async function fetchSupportResponse(prompt, sessionId) {
  const res = await fetch(`${process.env.NEXT_PUBLIC_API_URL}/support`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      prompt: [prompt],
      session_id: sessionId,
      run_id: `${Date.now()}`,
    }),
  });

  if (!res.ok) throw new Error("API call failed");
  return await res.json();
}
