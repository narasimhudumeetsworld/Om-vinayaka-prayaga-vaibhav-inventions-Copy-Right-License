#!/bin/bash

# License Validation Script
# Om Vinayaka 🙏
# Copyright (c) 2024-2025 Prayaga Vaibhav. All rights reserved.

echo "Om Vinayaka License Validation Script"
echo "====================================="
echo ""

# Function to check if file exists
check_file() {
    if [ -f "$1" ]; then
        echo "✅ $1 exists"
        return 0
    else
        echo "❌ $1 is missing"
        return 1
    fi
}

# Function to check if text exists in file
check_text_in_file() {
    if grep -q "$2" "$1" 2>/dev/null; then
        echo "✅ $1 contains required text: '$2'"
        return 0
    else
        echo "❌ $1 missing required text: '$2'"
        return 1
    fi
}

echo "Checking basic license files..."
echo "-----------------------------"

# Check for LICENSE file
check_file "LICENSE"

# Check for README.md
check_file "README.md"

echo ""
echo "Checking license content..."
echo "-------------------------"

# Check LICENSE file content
if [ -f "LICENSE" ]; then
    check_text_in_file "LICENSE" "Prayaga Vaibhav"
    check_text_in_file "LICENSE" "All Rights Reserved"
    check_text_in_file "LICENSE" "Om Vinayaka"
    check_text_in_file "LICENSE" "218+ inventions"
fi

echo ""
echo "Checking README content..."
echo "------------------------"

# Check README.md content
if [ -f "README.md" ]; then
    check_text_in_file "README.md" "Prayaga Vaibhav"
    check_text_in_file "README.md" "All Rights Reserved"
    check_text_in_file "README.md" "Copyright"
fi

echo ""
echo "Checking package files..."
echo "----------------------"

# Check package.json if exists
if [ -f "package.json" ]; then
    echo "Found package.json, checking content..."
    check_text_in_file "package.json" "Prayaga Vaibhav"
    check_text_in_file "package.json" "SEE LICENSE IN LICENSE"
fi

# Check setup.py if exists
if [ -f "setup.py" ]; then
    echo "Found setup.py, checking content..."
    check_text_in_file "setup.py" "Prayaga Vaibhav"
    check_text_in_file "setup.py" "Proprietary License"
fi

echo ""
echo "Checking source code headers..."
echo "-----------------------------"

# Check common source files for headers
for ext in "*.js" "*.py" "*.java" "*.cpp" "*.c" "*.h" "*.ts" "*.go"; do
    if ls $ext 1> /dev/null 2>&1; then
        echo "Checking $ext files for copyright headers..."
        for file in $ext; do
            if head -10 "$file" | grep -q "Prayaga Vaibhav"; then
                echo "✅ $file has proper copyright header"
            else
                echo "⚠️  $file may be missing copyright header"
            fi
        done
    fi
done

echo ""
echo "Validation Summary"
echo "=================="
echo ""
echo "Required Elements Checklist:"
echo "[ ] LICENSE file present"
echo "[ ] Copyright notice: © 2024-2025 Prayaga Vaibhav. All rights reserved."
echo "[ ] 'All Rights Reserved' declaration"
echo "[ ] 'Om Vinayaka 🙏' attribution"
echo "[ ] Contact information included"
echo "[ ] Repository link to license source"
echo "[ ] Media coverage provisions stated"
echo "[ ] Source files have copyright headers"
echo ""
echo "For manual verification, ensure:"
echo "1. All copyright dates are current (2024-2025)"
echo "2. Contact emails are: vaibhavlakshmi18@icloud.com, vaibhavlakshmi18@outlook.com, narasimhudumeetsworld@outlook.com"
echo "3. License link points to: https://github.com/narasimhudumeetsworld/Om-vinayaka-prayaga-vaibhav-inventions-Copy-Right-License"
echo "4. No conflicting license terms are present"
echo ""
echo "Contact for license questions: vaibhavlakshmi18@icloud.com"
echo ""
echo "Om Vinayaka 🙏"