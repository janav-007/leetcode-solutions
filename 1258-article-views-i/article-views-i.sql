SELECT DISTINCT views.author_id AS id
FROM views
WHERE views.author_id = views.viewer_id
ORDER BY id;