# Secure Coding Review Report

## Project

CodeAlpha Secure Coding Review

## Finding 1: Reflected Cross-Site Scripting (XSS)

**Affected file:** `vulnerable_app/app.py`  
**Severity:** High

The `/search` route returns user input directly in the page response:

```python
return f"You searched for: {query}"
```

Testing with HTML input showed that `<b>hello</b>` was rendered in bold. This confirms that the application interprets supplied input as HTML, which could allow malicious scripts to run in a visitor’s browser.

### Recommended Fix

Escape user-provided input before displaying it. The secure version uses:

```python
safe_query = escape(query)
```

This causes HTML tags to display as ordinary text rather than being executed or rendered.

## Finding 2: Debug Mode Enabled

**Affected files:** `vulnerable_app/app.py`, `secure_app/app.py`  
**Severity:** Medium

Both applications run with:

```python
app.run(debug=True)```

### Recommended Fix

Disable debug mode before deployment:

```python
app.run(debug=False)
```

## Conclusion

The vulnerable application contains a reflected XSS issue because it displays untrusted input directly. The secure application correctly escapes the search input and successfully prevents the issue. Debug mode should also be disabled for any production deployment.