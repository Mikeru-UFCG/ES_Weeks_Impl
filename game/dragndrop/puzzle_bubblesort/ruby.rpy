screen ruby_bs_puzzle:

    image "images/DragNDrop/bubblesort/ruby/background.jpg"

    draggroup:
        # Group of draggable pieces, and the spots they can be dragged to.
        # Paper pieces
        for i in range(page_pieces_ruby_bs):
            drag:
                drag_name i
                pos initial_line_coordinates_ruby_bs[i]
                anchor (0.5, 0.5)
                focus_mask True
                drag_raise True
                image "images/DragNDrop/bubblesort/ruby/piece%s.png" % (i + 1)

        # Snappable spots to drag to.
        for i in range(page_pieces_ruby_bs):
            drag:
                drag_name i
                draggable False
                droppable True
                dropped piece_drop_ruby_bs
                pos coordinate_lines_ruby_bs[i]
                anchor (0.5, 0.5)
                focus_mask True
                image "images/DragNDrop/bubblesort/ruby/piece%s.png" % (i + 1) alpha 0.0