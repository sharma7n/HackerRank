def group_by_marks(marks, pass_marks)
  # your code here
    def get_pass_key(marks, pass_marks)
        if marks < pass_marks
            "Failed"
        else
            "Passed"
        end
    end
    marks.group_by {|student, mark| get_pass_key(mark, pass_marks)}
end
